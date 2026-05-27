from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from resumes.models import Resume
from users.models import Profile
from homepage_user.mixins import NoCompanyRequiredMixin


class ResumeProfileView(NoCompanyRequiredMixin,TemplateView):
    template_name = 'resumes/profile_resume.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user= self.request.user
        resume = get_object_or_404(Resume,user=user)
        profile = get_object_or_404(Profile,user=user)
        context['profile'] = profile
        context['resume'] = resume
        return context