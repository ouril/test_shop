from django.contrib import auth
from django.http import Http404
from .forms import RegForm
from django.shortcuts import (
    render, 
    HttpResponseRedirect
)
from django.http import Http404

# Create your views here.
def login_form(request):
    return render(request, 'login.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = auth.authenticate(
            username = username, 
            password = password
            )
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/products')
        else:
            return HttpResponseRedirect('/products')

    raise Http404


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/products')


def registration(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/products')
        return render(request, 'registration.html', {'form': form})
    return render(request, 'registration.html', {'form': RegForm()})