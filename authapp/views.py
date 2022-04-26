from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, HttpResponseRedirect

from adminapp.forms import ProfileUpdateForm, UserUpdateForm
from authapp.forms import UserLoginForm, UserProfileEditForm, UserRegisterForm, UserEditForm
from django.contrib import auth
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from authapp.models import HabrUser
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.utils.timezone import now

from django.conf.urls import url

class SendVerifyMail:
    """ Отправка сообщения пользователю """

    def __init__(self, user):

        verify_link = reverse('auth:verify', args=[
            user.email, user.activation_key])  # Генерация ссылки

        subject = f'подтверждение учётной записи {user.username}'

        message = f'Для подтверждения учетной записи {user.username} на портале \
            {settings.DOMAIN_NAME} перейдите по ссылке: \n{settings.DOMAIN_NAME}{verify_link}'

        send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


class VerifyView(TemplateView):
    """ Проверка ключа активации """

    def get(self, request, email, activation_key):
        try:
            user = HabrUser.objects.get(email=email)
            if user.activation_key == activation_key and not user.is_activation_key_expired():
                user.is_active = True
                user.activation_key = None
                # Думаю при обнулении ключа лучше и сроки сдвинуть до текущего момента
                user.activation_key_expires = now()
                user.save()
                auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return HttpResponseRedirect(reverse('main'))
            else:
                print(f'ошибка активации пользователя: {user}')
                return render(request, 'authapp/verification.html')
        except Exception as ex:
            return HttpResponseRedirect(reverse('main'))

# @csrf_exempt
class LoginUserView(LoginView):
    """ Контроллер входа в системы """
    template_name = 'authapp/login.html'
    form_class = UserLoginForm


class LogoutUserView(LogoutView):
    """ Контроллер выхода из системы """
    pass


class RegisterUserView(SuccessMessageMixin, CreateView):
    template_name = 'authapp/register.html'
    success_url = reverse_lazy('auth:login')
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"

    def post(self, request, *args, **kwargs):
        """ Проверяем форму регистрации """

        register_form = UserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            if HabrUser.objects.all().filter(email=register_form.data['email']):
                context = {'error': f'пользователь уже зарегистрирован с данным EMAIL:{register_form.data["email"]}'}
                return render(request, 'authapp/error.html', context)
            user = register_form.save()
            SendVerifyMail(user)
            return HttpResponseRedirect(reverse('auth:login'))


class ProfileEditView(LoginRequiredMixin, UpdateView):
    """ Редактирование профиля """

    model = HabrUser
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('_admin:users')
    form_class = UserUpdateForm
    second_form_class = ProfileUpdateForm

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(instance=self.object)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=self.object.habrprofile)
        context['avatar'] = self.object.avatar
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form2 = self.second_form_class(request.POST, instance=self.object.habrprofile)
        form = self.form_class(request.POST, instance=self.object)
        if form.is_valid() and form2.is_valid():
            form2.save()
            return super().post(request, *args, **kwargs)
        else:
            return self.render_to_response(
                self.get_context_data(form=form, form2=form2))



# def edit(request):
#     title = 'редактирование'
#
#     if request.method == 'POST':
#         edit_form = UserEditForm(
#             request.POST, request.FILES, instance=request.user)
#         profile_form = UserProfileEditForm(
#             request.POST, instance=request.user.userprofile)
#         if edit_form.is_valid() and profile_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('auth:edit'))
#     else:
#         edit_form = UserEditForm(instance=request.user)
#         profile_form = UserProfileEditForm(
#             instance=request.user.shopuserprofile)
#
#     content = {'title': title, 'edit_form': edit_form,
#                'profile_form': profile_form}
#
#     return render(request, 'authapp/edit.html', content)
