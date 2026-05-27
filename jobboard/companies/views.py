from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views.decorators.http import require_http_methods
from companies.models import FavoriteVacancy, Vacancy, HiddenVacancy
from homepage_user.mixins import NoCompanyRequiredMixin


@login_required
def toggle_favorite(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, id=vacancy_id)
    favorite_vacancy, created = FavoriteVacancy.objects.get_or_create(
        user=request.user, vacancy=vacancy
    )
    if not created:
        favorite_vacancy.delete()
        return JsonResponse({"status": "removed"})
    else:
        return JsonResponse({"status": "added"})


@login_required
@require_http_methods(["POST"])
def toggle_hidden(request):
    vacancy = get_object_or_404(Vacancy, id=request.POST.get("vacancy_id"))
    hidden_vacancy, created = HiddenVacancy.objects.get_or_create(
        user=request.user, vacancy=vacancy
    )
    if not created:
        hidden_vacancy.delete()
        return JsonResponse({"status": "removed"})
    else:
        return JsonResponse({"status": "hidden"})


class HiddenVacancyForUser(NoCompanyRequiredMixin, TemplateView):
    template_name = "companies/hidden_vacancies.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        hidden_vacancy = HiddenVacancy.objects.filter(user=user).select_related(
            "vacancy"
        )
        context["hidden_vacancies"] = hidden_vacancy
        context["has_hidden"] = hidden_vacancy.exists()
        return context
