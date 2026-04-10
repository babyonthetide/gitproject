from django.contrib import admin
from .models import Company, Vacancy,FeedbackCompany
# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'website', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name','owner__username')


    def average_rating_display(self,object):
        return object.average_rating()

    average_rating_display.short_description = 'Средняя оценка'

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id','title','company','employment_type','schedule','created_at')
    list_filter = ('employment_type','schedule','created_at')
    search_fields = ('title','company__name')


@admin.register(FeedbackCompany)
class FeedBackCompanyAdmin(admin.ModelAdmin):
    list_display = ('id','company','comment','rating','created_at')
    list_filter = ('rating','created_at')
    search_fields = ('company__name','comment')
