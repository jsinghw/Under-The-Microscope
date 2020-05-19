from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.conf import settings

from app.forms import LoginForm, SignUpForm
from app.models import CustomUser


# Create your views here.
@login_required
def index(request):
    data = request.user
    return render(request, 'index.html', {'data': data, 'settings': settings})


# SignUpForm Help
# https://dev.to/coderasha/create-advanced-user-sign-up-view-in-django-step-by-step-k9m
def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return HttpResponseRedirect(reverse('homepage'))
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    html = 'login.html'

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data['username'],
                password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', 'index.html')
                )
    form = LoginForm()
    return render(request, html, {'form': form})


def logout_view(request):
    if request.user:
        logout(request)
    return HttpResponseRedirect(reverse('homepage'))
