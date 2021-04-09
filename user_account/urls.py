from django.conf import settings
from django.templatetags.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup', views.signup, name='signup'),
]
