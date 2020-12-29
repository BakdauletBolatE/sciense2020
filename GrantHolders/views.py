from django.shortcuts import render,redirect
from .models import GrantHolders,Like
from django.contrib.auth.models import User
from .forms import LikeForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect


# Create your views here.
def home(request):
    queryset = GrantHolders.objects.order_by('-graduate_year')
    return render(request, 'GrantHolders/list_view.html',{'qhols':queryset})

def homeapi(request):
    queryset = GrantHolders.objects.all()
    return json.dumps(queryset)


def GDetailview(request,url):
    grantHolders = GrantHolders.objects.get(slug=url)
    like = Like.objects.filter(post=grantHolders)
    isLiked = None
    if request.user.is_authenticated:
        try:
            isLiked = Like.objects.get(user=request.user,post=grantHolders)
        except Like.DoesNotExist:
            isLiked = None

    # isLiked = Like.objects.get(user=request.user, post=grantHolders) # select * like where user_id = ...

    return render(request,'GrantHolders/detailview.html',{'qhol':grantHolders,'like':like, 'isLiked': isLiked})

@login_required(login_url='home')
def like(request,url):
    if request.method == 'POST':
        user = request.user
        if user.is_authenticated:
            post = GrantHolders.objects.get(slug=url)
            like = Like.objects.create(user=user,post=post)
            return redirect('detailview',url)
        else:
            pass
           
        
