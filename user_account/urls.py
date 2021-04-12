from django.conf.urls import url
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = (
    path('', views.home, name='home'),
    path('signin/', views.login_user, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('signout/', views.logout_user, name='signout'),
    path('loan/', views.loan_app, name='loan'),
    path('password-change/',
         auth_views.PasswordChangeView.as_view(template_name='user_accounts/password_change.html'),
         name='password_change'),
    path('password-change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='user_accounts/password_change_done.html'),
         name='password_change_done'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='user_accounts/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='user_accounts/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='user_accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='user_accounts/password_reset_complete.html'),
         name='password_reset_complete'),
)
