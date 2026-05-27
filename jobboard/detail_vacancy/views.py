from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import DetailView
from companies.models import Vacancy, Company, FeedbackCompany, FavoriteVacancy, HiddenCompany
from core.models import SiteSettings
from users.models import Profile
from detail_vacancy.utils import render_stars_html,years_declension,split_lines
from django.contrib import messages
from companies.models import HiddenVacancy
from django.contrib.auth.decorators import login_required
from companies.forms import ComplaintForm
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

@login_required
def hide_vacancy(request,pk):
    if request.method =='POST':
        vacancy = get_object_or_404(Vacancy,id=pk)
        HiddenVacancy.objects.get_or_create(user=request.user,vacancy=vacancy)
        messages.success(request,"Вакансия скрыта")
    return redirect("homepage_user:homepage")


@login_required
def hide_company(request,pk):
    if request.method == 'POST':
        company = get_object_or_404(Company,id=pk)
        hidden_company, created = HiddenCompany.objects.get_or_create(company=company,user=request.user)
        if created:
            messages.success(request,'Компания скрыта и больше не будет отображаться.')
        else:
            messages.success(request,'Компания уже скрыта.')
    return redirect("homepage_user:homepage")


@login_required
def submit_complaint(request,pk):
    vacancy = get_object_or_404(Vacancy,id=pk)
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user
            complaint.vacancy = vacancy
            complaint.save()
            messages.success(request,'Ваша жалоба успешно отправлена')
            return redirect("detail_vacancy:detail_vacancy",pk=vacancy.id)
    else:
        form = ComplaintForm()
    context = {'form':form,
               'vacancy':vacancy}
    return render(request,'detail_vacancy/complaint.html',context)