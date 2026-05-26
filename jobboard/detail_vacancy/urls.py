from django.urls import path
from detail_vacancy import views

app_name = 'detail_vacancy'
urlpatterns = [
    path('vacancy/<int:pk>/',views.DetailVacancyView.as_view(),name='detail_vacancy'),
    path('hide/vacancy/<int:pk>/',views.hide_vacancy,name='hide_vacancy'),
    path('hide/company/<int:pk>/',views.hide_company,name='hide_company')
]