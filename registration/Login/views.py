from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def loginpage(request):
    if request.method == 'POST':
        usern = request.POST.get('user')
        pass1 = request.POST.get('pass')
        var=authenticate(request,username=usern,password=pass1)
        if var is not None:
            login(request,var)
            return redirect('home')
        else:
            return HttpResponse("Incorrect credentials")

    return render(request,"loginpage.html")

def signpage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 != pass2:
            return HttpResponse("your Password doesn't matched")
        else:
          my_user=User.objects.create_user(uname,pass1,pass2)
          my_user.save()
        return redirect('login')
    return render(request,"signup.html")


@login_required(login_url='login')
def homepage(request):
    return render(request, "Home.html")

def logoutpage(request):
    logout(request)
    return redirect('login')