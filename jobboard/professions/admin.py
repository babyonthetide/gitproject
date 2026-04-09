from django.contrib import admin
from professions.models import Profession,CategoryProfession
# Register your models here.


class InlineProfession(admin.TabularInline):
    model = Profession
    extra = 1


@admin.register(CategoryProfession)
class CategoryProfessionAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_filter = ('name',)
    search_fields = ('name',)
    inlines = [InlineProfession]

@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('category','name','description')
    list_filter = ('category',)
    search_fields = ('name','category__name')