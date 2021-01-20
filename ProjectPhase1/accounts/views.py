from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import SignUpForm, UserForm, ProfileForm
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .decorators import unauthenticated_user

@unauthenticated_user
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form' : form})

