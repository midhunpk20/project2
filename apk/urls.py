from django.urls import path
from .views import *

urlpatterns = [
    path('',user_register,name="register_link"),
    path('login_page',user_login,name="login_link"),
    path('user_logout',user_logout,name="logout_link"),
    path('home_page',user_home,name="home_link"),
    path('contact_page',user_contact,name="contact_link")
    
]
