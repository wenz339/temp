from django.shortcuts import render
from django.contrib.auth import authenticate , login ,logout
from django.shortcuts import redirect

from django.contrib import messages
from store.forms import CustomUserForm

def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registered Sucessfully")
            return redirect('/login')
    context = {'form':form}
    return render(request,"store/template/store/auth/register.html",context)

def loginpage(request):
    if request.user.is_authenticated:
        messages.success(request,"You are already login")
        return redirect('/')
    
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')

            user = authenticate(request, username = name,password = passwd)

            if user is not None:
                login(request,user)
                messages.success(request,"Login Successfully")
                return redirect("/")
            else:
                messages.error(request,"Invalid Username or Password")
                return redirect('/login')
        return render(request,"store/template/store/auth/login.html")
    
def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logout Successfully")
    return redirect("/")
