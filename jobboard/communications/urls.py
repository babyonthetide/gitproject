from django.urls import path
from communications import views

app_name = "communications"
urlpatterns = [
    path("send-response/<int:id>/", views.ResponseView, name="send_response"),
]
