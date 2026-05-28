from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("homepage_user.urls", namespace="homepage_user")),
    path("vacancy/", include("companies.urls", namespace="companies")),
    path("detail/", include("detail_vacancy.urls", namespace="detail_vacancy")),
    path("resume/", include("resumes.urls", namespace="resumes")),
    path("communications/", include("communications.urls", namespace="communications")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
