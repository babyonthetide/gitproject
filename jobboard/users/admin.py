from django.contrib import admin
from .models import Profile
# Register your models here.


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ("user", "phone", "location", "is_verified", "created_at")
    list_filter = ("is_verified", "created_at")
    search_fields = ("user__username", "phone", "location")

