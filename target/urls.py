from target import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import login_view

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    #path('forget/', views.forget_password, name='forget_password'),
    # django built in provide password change, reset etc.
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    #path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    #path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]


