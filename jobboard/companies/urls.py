from django.urls import path
from companies import views
app_name='companies'
urlpatterns = [
    path('toggle/<int:vacancy_id>/',views.toggle_favorite,name='toggle_favorite'),
    path('toggle-hidden-vacancy/',views.toggle_hidden,name='hidden_vacancy'),
]