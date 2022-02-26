from account.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render,redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login , authenticate,logout
from django.contrib.auth.decorators import login_required
from .forms import UpdateForm

# # Create your views here.

def register(request):
    if request.user.username:
        return redirect('/doctor')
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/login')
    return render(request, 'signup.html', {'form': form})

def login_user(request):
    if request.user.username:
        return redirect('/doctor')
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        email=request.POST['username']
        password=request.POST['password']
        user= authenticate(username=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('/login')

@login_required(login_url='/login')
def index(request):
    all=User.objects.all()
    return render(request,'index.html',{'data':all})

@login_required(login_url='/login')
def deleteUser(request,pk):
    user=User.objects.filter(pk=pk)
    print("deleted successfull")
    user.delete()
    return redirect('/')

@login_required(login_url='/login')
def update_user(request):
    id=request.GET['user_id']
    user=User.objects.get(id=id)
    form=UpdateForm(request.POST or None,instance=user)
    if request.method=='POST':
        form=UpdateForm(request.POST,instance=user)
        if form.is_valid():
            obj=form.save()
            img=request.FILES.get('profile_picture')
            if img:
                obj.profile_picture=img
                obj.save()
            return redirect('/')
    return render(request,'edit.html',{'user':user,'form':form})

@login_required(login_url='/login')
def doctor(request):
    if request.user.level=='Patient':
        return redirect('/patient')
    return render(request,'doctor.html')

@login_required(login_url='/login')
def patient(request):
    if request.user.level=='Doctor':
        return redirect('/doctor')
    return render(request,'patient.html')