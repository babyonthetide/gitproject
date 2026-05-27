from django.urls import path
from resumes.views import ResumeProfileView, edit_resume

app_name = "resumes"
urlpatterns = [
    path("info/", ResumeProfileView.as_view(), name="resume_profile_view"),
    path("edit/", edit_resume, name="resume_edit"),
]
