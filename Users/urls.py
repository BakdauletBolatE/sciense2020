from django.urls import path
from .views import loginn,register,logoutUser,like_list

urlpatterns = [
    path('register/', register,name="register"),
    path('login/',loginn,name="loginn"),
    path('logout/',logoutUser,name="logout"),
    path('like_lists/',like_list,name="like_list")
]