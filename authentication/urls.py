from django.urls import path
from . import views

urlpatterns = [
    # Views
    path('', views.login_view ,name="login"),
    path('signin/', views.signin_view, name='signin'),
    
    # Functions
    path('dosignup/', views.dosignin_ep, name='dosignup'), 
]