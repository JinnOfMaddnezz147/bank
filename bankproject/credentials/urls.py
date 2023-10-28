from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('logouttomenu/', views.logouttomenu, name='logouttomenu'),
    path('form/', views.form, name='form'),
    path('submit/', views.submit_data, name='submit_data'),
]
