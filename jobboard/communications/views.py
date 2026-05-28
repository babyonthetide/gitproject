from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from communications.models import Response
from companies.models import Vacancy
from resumes.models import Resume


@login_required
def ResponseView(request, id):
    if request.method == "POST":
        vacancy = Vacancy.objects.get(id=id)
        resume = Resume.objects.get(user=request.user)
        response, created = Response.objects.get_or_create(
            vacancy=vacancy, resume=resume
        )
        if created:
            return JsonResponse({"created": "ok", "status": response.status})
        else:
            return JsonResponse({"response_id": response.id, "status": response.status})
