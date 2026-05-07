from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render,get_object_or_404
from companies.models import FavoriteVacancy,Vacancy

@login_required
def toggle_favorite(request,vacancy_id):
    vacancy = get_object_or_404(Vacancy,id=vacancy_id)
    favorite_vacancy,created = FavoriteVacancy.objects.get_or_create(user=request.user,vacancy=vacancy)
    if not created:
        favorite_vacancy.delete()
        return JsonResponse({'status':'removed'})
    else:
        return JsonResponse({'status':'added'})
