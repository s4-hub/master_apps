from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Profil
from .forms import LoginForm, ProfilEditForm

@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                login(request, user)
                return HttpResponse('Konfirmasi berhasil')
            else:
                return HttpResponse('Akun di nonaktifkan account')
        else:
            return HttpResponse('Info masuk tidak valid')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

@login_required
def edit(request):
    if request.method == 'POST':
       
        profil_form = ProfilEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES)
        if profil_form.is_valid():
            
            profil_form.save()
            messages.success(request, 'Profile updated '
                             'successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
       
        profil_form = ProfilEditForm(
            instance=request.user.profil)

    return render(request,
                  'account/edit.html',
                  {
                   'profil_form': profil_form})