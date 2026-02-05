from django.urls import path
from .views import superuser_login, dashboard, logout_view

urlpatterns = [
    path("login/", superuser_login, name="login"),
    path("dashboard/", dashboard, name="dashboard"),
    path("logout/", logout_view, name="logout"),
]
