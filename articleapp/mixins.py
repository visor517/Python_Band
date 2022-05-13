from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect


class UserIsNoBlockMixin(UserPassesTestMixin):
    """ Предоставляет право доступа пользователю который не заблокирован """

    def test_func(self):
        user = self.request.user
        if user.is_authenticated:
            return user.check_block() is False

    def handle_no_permission(self):
        return redirect('/')
