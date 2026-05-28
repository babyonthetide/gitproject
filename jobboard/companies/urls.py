from django.urls import path
from companies import views

app_name = "companies"
urlpatterns = [
    path("toggle/<int:vacancy_id>/", views.toggle_favorite, name="toggle_favorite"),
    path("toggle-hidden-vacancy/", views.toggle_hidden, name="hidden_vacancy"),
    path(
        "hidden-list/", views.HiddenVacancyForUser.as_view(), name="hidden_vacancy_list"
    ),
    path(
        "favorite-list/",
        views.FavoriteVacancyForUser.as_view(),
        name="favorite_vacancy_list",
    ),
]
