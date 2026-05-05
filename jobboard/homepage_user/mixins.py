from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse


class NoCompanyRequiredMixin(LoginRequiredMixin,UserPassesTestMixin):
    login_url = '/accounts/login/'
    redirect_company_url_name = 'some_company_dashboard_url'

    def test_func(self):
        #Проверяем наличие компании у пользователя
        return not (hasattr(self.request.user, 'company') and self.request.user.company is not None)

    def handle_no_permission(self):
        #Перенаправляем на страницу компании, если пользователь не прошёл проверку в test_func
        if self.request.user.is_authenticated:
            return redirect(reverse(self.redirect_company_url_name))
        return super().handle_no_permission()  # Передаем обработку неавторизованных пользователей