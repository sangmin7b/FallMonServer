from django.urls import path
from . import views

urlpatterns = [
    path("fall_history", views.fall_history_view),
    path("fall_history_user", views.get_fall_history_by_user),
    path("user", views.user_view),
]