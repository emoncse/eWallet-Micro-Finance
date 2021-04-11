from django.conf import settings
from django.templatetags.static import static
from django.urls import path, include
from . import views

urlpatterns = (
    path('', views.home, name='home'),
    path('signin/', views.login_user, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('signout/', views.logout_user, name='signout'),
)
