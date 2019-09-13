from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import Userregisterform,UserUpdateForm,UserProfileForm

def register(request):
    if request.method=='POST':
         form=Userregisterform(request.POST)
         if form.is_valid():
             form.save()
             username=form.cleaned_data.get('username')
             messages.success(request,f'Your account has been created! Now you able to log In.')
             return redirect('login')
    else:
        form=Userregisterform()
    return render(request,'users/register.html',{'form':form})   

@login_required
def profile(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST, instance=request.user)
        p_form=UserProfileForm(request.POST,
                               request.FILES,
                               instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=UserProfileForm(instance=request.user.profile)

    context={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'users/profile.html',context)
       


    