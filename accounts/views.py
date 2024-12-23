from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def register(request):
    # Register new users
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form=UserCreationForm(data=request.POST)
        if form.is_valid :
            new_user = form.save()
            login(request,new_user)
            return redirect('blogs:index')

    #Display blank  or invalie form
    context={'form':form}
    return render(request,'registration/register.html',context)
        