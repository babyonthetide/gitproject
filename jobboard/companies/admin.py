from django.contrib import admin
from .models import Company, Vacancy
# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'website', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name','owner__username')


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id','title','company','employment_type','schedule','created_at')
    list_filter = ('employment_type','schedule','created_at')
    search_fields = ('title','company__name')
