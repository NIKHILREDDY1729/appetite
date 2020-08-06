from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from home.models import receipe
from .forms import CreateUserForm


# Create your views here.
def Feed(request):
    rec = receipe.objects.all()
    print(rec)
    context = {'rec':rec}
    return render(request, 'Feed.html', context)
  
def Browse(request):
    return render(request,'Browse.html') 

def Articles(request):
    return render(request,'Articles.html')

def userprofile(request):
    return render(request,'userprofile.html')  
def form(request):
    if request.method == "POST":
        name = request.POST.get(str('name'))
        image =request.POST.get('image')
        desc = request.POST.get('desc')
        time=request.POST.get('time')
        Rece= receipe(name=name,image=image,desc=desc,time=time)
        Rece.save()
        messages.success(request, 'Your reciepe has been uploaded!')
    return render(request,'form.html') 
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('userprofile')
        else:
            messages.info(request,'Username or Password is incorrect')    
    return render(request,'Login.html')

def Register(request):
    form =CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'account was created for ' + ' '+user)
            return redirect('Login')
    context={'form':form}
    return render(request,'Register.html',context)
 