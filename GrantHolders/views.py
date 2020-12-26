from django.shortcuts import render
from .models import GrantHolders

# Create your views here.
def home(request):
    queryset = GrantHolders.objects.all()
    return render(request, 'GrantHolders/list_view.html',{'qhols':queryset})


def GDetailview(request,url):
    queryset = GrantHolders.objects.get(slug=url)
    return render(request,'GrantHolders/detailview.html',{'qhol':queryset})