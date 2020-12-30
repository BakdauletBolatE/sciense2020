from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail  
from django.shortcuts import HttpResponseRedirect




def sendMail(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            
            if mail:
                messages.success(request,'Сіздің өтініміз жіберілді')
                return redirect('home')
            else:
                messages.error(request,'Жіберілмеді')
                return redirect('home')





def register(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            userL = authenticate(request,username=user,password=password)
            dataS = f"Құрметті {user}"
            dataC = """Сіз Silkway университетінің білім ғылым иегерлер сайтына сәтті 
             тіркелдіңіз грант иегерлеріне лайк басып соңғы жаңалықтарды көрсеңіз 
             болады"""
            mail = send_mail(dataS, dataC, 'b.fead@mail.ru',[form.cleaned_data['email']],fail_silently=False)
            login(request,userL)
            messages.success(request,f"Сіз {user} сәтті тіркелдіңіз")

            return redirect('home')

    context = {
        'form': form,
    }
    
        
    return render(request,'accounts/register.html',context)


def loginn(request):
    form = CreateUserForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)

            messages.success(request,f"Сіз {user} сәтті жүйеге кірдіңіз")
            return redirect('home')
    context = {
        'form': form,
    }
    
    return render(request,'accounts/login.html',context)

def logoutUser(request):
   logout(request)
   return redirect('home')

@login_required(login_url='user:register')
def like_list(request):
    user = request.user
    like = user.likes.all()
    context = {
        'qhols':like
    }
    return render(request,"Users/like_list.html",context)
    
    
