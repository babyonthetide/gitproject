from django.shortcuts import render
from django.views.generic import TemplateView
from companies.models import Vacancy
from core.models import SiteSettings
from communications.models import Invitation,Response

class HomePageView(TemplateView):
    template_name = 'homepage_user/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #Получаем настройки сайта, логотип и баннер
        site_settings = SiteSettings.objects.first()
        context['logo'] = site_settings.logo if site_settings.logo else None
        context['main_banner'] = site_settings.main_banner if site_settings.main_banner else None
        #Получаем количество откликов и приглашений
        total_responses = Response.objects.count()
        total_invitation = Invitation.objects.count()
        context['total_responses'] = total_responses
        context['total_invitation'] = total_invitation
        #Получаем 7 последних вакансий
        context['vacansies'] = Vacancy.objects.select_related('company','profession').all()[:7]
        return context