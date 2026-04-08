from django.contrib import admin
from .models import Company
# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'website', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name','owner__username')

