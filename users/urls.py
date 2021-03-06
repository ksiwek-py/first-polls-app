from django.urls import path
from django.contrib.auth import views as auth_views
from users import views as user_views

app_name = 'users'

urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('user/<username>/', user_views.PublicProfile
         .as_view(template_name='users/public_profile.html'), name='public_profile'),
]
