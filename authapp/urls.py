from django.urls import path

from .views import LoginUserView, LogoutUserView, RegisterUserView, VerifyView, ProfileEditView
from django.conf.urls import include, url

app_name = 'authapp'

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('edit/<int:pk>/', ProfileEditView.as_view(), name='edit'),
    path('verify/<email>/<activation_key>', VerifyView.as_view(), name="verify"),
]
