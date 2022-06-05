from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('dashboard/',views.dashboardView,name="dashboard"), # localhost:8000/reg/dashboard
    path('login/',LoginView.as_view(),name="login_url"),
    path('register/',views.registerView,name="register_url"),
    path('logout/',LogoutView.as_view(next_page='homepage'),name="logout"),
]