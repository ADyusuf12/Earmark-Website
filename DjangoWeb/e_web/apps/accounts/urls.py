from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import ProfileView


app_name="accounts"
urlpatterns = [
    
    
    path('profile/', ProfileView.as_view(), name="profile"),
    path('profile/<int:pk>/', ProfileView.as_view(), name='user-profile-detail'),
    path("login", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", views.register, name="register"),
    path("profile-settings/", views.ProfileSettings, name="profile-settings"),
    

]