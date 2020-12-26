from django.urls import path
from .views import home,GDetailview

urlpatterns = [
    path('',home,name="home"),
    path('graduate/<slug:url>/',GDetailview,name="detailview")
]