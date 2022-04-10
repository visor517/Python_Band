from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import UserLoginForm, UserProfileEditForm, UserRegisterForm, UserEditForm
from django.contrib import auth
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from authapp.models import HabrUser

from django.utils.timezone import now


def send_verify_mail(user):
    verify_link = reverse('auth:verify', args=[
                          user.email, user.activation_key])  # Генерация ссылки

    subject = f'подтверждение учётной записи {user.username}'

    message = f'Для подтверждения учетной записи {user.username} на портале \
        {settings.DOMAIN_NAME} перейдите по ссылке: \n{settings.DOMAIN_NAME}{verify_link}'

    return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def verify(request, email, activation_key):

    try:
        user = HabrUser.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            user.activation_key = None
            # Думаю при обнулении ключа лучше и сроки сдвинуть до текущего момента
            user.activation_key_expires = now()
            user.save()
            auth.login(request, user)
            return render(request, 'authapp/verification.html')
        else:
            print(f'ошибка активации пользователя: {user}')
            return render(request, 'authapp/verification.html')
    except Exception as ex:
        return HttpResponseRedirect(reverse('main'))

# @csrf_exempt
def login(request):
    title = 'вход'

    login_form = UserLoginForm(data=request.POST or None)

    next = request.GET['next'] if 'next' in request.GET.keys() else ''
    #print('next', next)

    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse('main'))

    content = {
        'title': title,
        'login_form': login_form,
        'next': next
    }

    return render(request, 'authapp/login.html', content)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


def register(request):
    title = 'регистрация'

    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            if HabrUser.objects.all().filter(email=register_form.data['email']):
                context = {'error': f'пользователь уже зарегистрирован с данным EMAIL:{register_form.data["email"]}'}
                return render(request, 'authapp/error.html', context)
            user = register_form.save()
            if send_verify_mail(user):
                print("success")
            else:
                print("failed")
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = UserRegisterForm()

    content = {'title': title, 'register_form': register_form}

    return render(request, 'authapp/register.html', content)


def edit(request):
    title = 'редактирование'

    if request.method == 'POST':
        edit_form = UserEditForm(
            request.POST, request.FILES, instance=request.user)
        profile_form = UserProfileEditForm(
            request.POST, instance=request.user.userprofile)
        if edit_form.is_valid() and profile_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = UserEditForm(instance=request.user)
        profile_form = UserProfileEditForm(
            instance=request.user.shopuserprofile)

    content = {'title': title, 'edit_form': edit_form,
               'profile_form': profile_form}

    return render(request, 'authapp/edit.html', content)
