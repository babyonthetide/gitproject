from django.urls import path
from resumes.views import ResumeProfileView

app_name = 'resumes'
urlpatterns = [
    path('info/',ResumeProfileView.as_view(),name='resume_profile_view'),
    ]