from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from resumes.forms import ResumeForm
from resumes.models import Resume
from users.models import Profile
from homepage_user.mixins import NoCompanyRequiredMixin
from django.contrib import messages


class ResumeProfileView(NoCompanyRequiredMixin, TemplateView):
    template_name = "resumes/profile_resume.html"

    def get(self, request, *args, **kwargs):
        user = request.user
        try:
            resume = Resume.objects.get(user=user)
            profile = Profile.objects.get(user=user)
        except (Resume.DoesNotExist, Profile.DoesNotExist):
            return redirect("resumes:resume_edit")
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        resume = get_object_or_404(Resume, user=user)
        profile = get_object_or_404(Profile, user=user)
        context["profile"] = profile
        context["resume"] = resume
        return context


@login_required
def edit_resume(request):
    user = request.user
    try:
        resume = Resume.objects.get(user=user)
    except Resume.DoesNotExist:
        resume = Resume(user=user)
    if request.method == "POST":
        form = ResumeForm(request.POST, instance=resume)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = user
            resume.save()
            messages.success(request, "Данные сохранены")
            return redirect("resumes:resume_profile_view")
    else:
        form = ResumeForm(instance=resume)
    context = {"user": user, "resume": resume, "form": form}
    return render(request, "resumes/edit_resume.html", context)
