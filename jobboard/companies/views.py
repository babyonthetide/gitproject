from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render,get_object_or_404
from django.views.decorators.http import require_http_methods
from companies.models import FavoriteVacancy,Vacancy,HiddenVacancy

@login_required
def toggle_favorite(request,vacancy_id):
    vacancy = get_object_or_404(Vacancy,id=vacancy_id)
    favorite_vacancy,created = FavoriteVacancy.objects.get_or_create(user=request.user,vacancy=vacancy)
    if not created:
        favorite_vacancy.delete()
        return JsonResponse({'status':'removed'})
    else:
        return JsonResponse({'status':'added'})


@login_required
@require_http_methods(['POST'])
def toggle_hidden(request):
    vacancy = get_object_or_404(Vacancy,id=request.POST.get('vacancy_id'))
    hidden_vacancy, created = HiddenVacancy.objects.get_or_create(user=request.user,vacancy=vacancy)
    if not created:
        hidden_vacancy.delete()
        return JsonResponse({'status':'removed'})
    else:
        return JsonResponse({'status':'hidden'})