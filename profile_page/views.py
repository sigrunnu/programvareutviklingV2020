from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required



@login_required
def profile(request):
    context = {
        'fullName': 'Andreas Amundsen',
        'username': 'testomundsen',
        'email': 'roids@biceps.com',

    }

    return render(request, 'profile_page/profile_view.html', context)



def signupView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {'form': form})

def LoginView(request):
    return render(request, "registration/login.html")
