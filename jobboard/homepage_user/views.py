from django.shortcuts import render
from django.template.context_processors import request
from django.views.generic import TemplateView
from companies.models import Vacancy,FavoriteVacancy
from core.models import SiteSettings
from communications.models import Invitation,Response
from homepage_user.mixins import NoCompanyRequiredMixin
from resumes.models import ResumeView
from homepage_user.utils import filterd_objects_with_filter_type
from users.models import Profile

class HomePageView(NoCompanyRequiredMixin,TemplateView):
    template_name = 'homepage_user/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #Получаем выбранный фильтр
        filter_type = self.request.GET.get('filter')
        #Получаем настройки сайта, логотип и баннер
        site_settings = SiteSettings.objects.first()
        context['logo'] = site_settings.logo if site_settings.logo else None
        context['main_banner'] = site_settings.main_banner if site_settings.main_banner else None
        context['city'] = Profile.objects.get(user=self.request.user).get_city_display()
        #Получаем количество откликов и приглашений
        total_responses = Response.objects.count()
        total_invitation = Invitation.objects.count()
        #Количество просмотров резюме
        total_resume_views = ResumeView.objects.count()
        #Количество избранных вакансий
        total_favorite_vacancy = FavoriteVacancy.objects.count()
        context['total_favorite_vacancy'] = total_favorite_vacancy
        context['total_resume_views'] = total_resume_views
        context['total_responses'] = total_responses
        context['total_invitation'] = total_invitation
        #Получаем 7 последних вакансий
        vacancies = Vacancy.objects.select_related('company','profession').exclude(hidden_by_user__user=self.request.user)
        filtered_vacancies = filterd_objects_with_filter_type(vacancies,filter_type)[:7]
        #Избранные вакнасии
        context['user_favorites'] = FavoriteVacancy.objects.filter(user=self.request.user).values_list('vacancy_id', flat=True)
        context['vacancies'] = filtered_vacancies
        return context