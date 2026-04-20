from django.contrib import admin
from .models import Response

@admin.register(Response)
class AdminResponse(admin.ModelAdmin):
    list_display = ('vacancy','resume','status','created_at')
    list_filter = ('status','created_at')
    search_fields = ('vacancy__title','resume__last_name')


