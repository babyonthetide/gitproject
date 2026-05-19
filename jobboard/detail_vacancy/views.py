from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.template.context_processors import request
from django.views.generic import DetailView
from companies.models import Vacancy, Company, FeedbackCompany, FavoriteVacancy
from core.models import SiteSettings
from users.models import Profile
from detail_vacancy.utils import render_stars_html,years_declension,split_lines

# Create your views here.

class DetailVacancyView(LoginRequiredMixin,DetailView):
    model = Vacancy
    template_name = 'detail_vacancy/detail_vacancy.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vacancy = context['vacancy']
        # Получаем настройки сайта, логотип и баннер
        site_settings = SiteSettings.objects.first()
        context['logo'] = site_settings.logo if site_settings.logo else None
        context['main_banner'] = site_settings.main_banner if site_settings.main_banner else None
        #Город пользователя
        context['user_city'] = get_object_or_404(Profile,user=self.request.user).get_city_display()
        #Другие вакансии компании
        context['vacancies_company'] = Vacancy.objects.filter(company=vacancy.company).exclude(
            id=vacancy.pk,
            hidden_by_user__user=self.request.user)
        #Похожие вакансии от других компаний
        context['similar_vacancies'] = Vacancy.objects.exclude(
            id=vacancy.pk,
            company=vacancy.company,
            hidden_by_user__user=self.request.user)[:2]
        context['feedbacks_company'] = FeedbackCompany.objects.filter(company=vacancy.company)[:4]
        #Рейтинг и звёзды
        context['rating'] = vacancy.company.average_rating()
        context['stars_rating'] = render_stars_html(rating=context['rating'])
        #Опыт работы
        context['experience_required'] = years_declension(
            vacancy.experience_required,
            vacancy.experience_from,
            vacancy.experience_to
        )
        context['responsibilities'] = split_lines(vacancy.responsibilities)
        context['conditions'] = split_lines(vacancy.conditions)
        #Список избранных вакансий
        context['user_favorites'] = FavoriteVacancy.objects.filter(user=self.request.user).values_list('vacancy_id', flat=True)
        return context