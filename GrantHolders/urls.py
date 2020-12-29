from django.urls import path
from .views import home,GDetailview,like,homeapi

urlpatterns = [
    path('',home,name="home"),
    path('graduate/<slug:url>/',GDetailview,name="detailview"),
    path('like/<slug:url>/',like,name="like"),
    path('api/',homeapi,name="homepai")
]