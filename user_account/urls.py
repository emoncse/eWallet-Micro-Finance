from django.urls import path
from . import views

urlpatterns = (
    path('', views.home, name='home'),
    path('signin/', views.login_user, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('signout/', views.logout_user, name='signout'),
)
