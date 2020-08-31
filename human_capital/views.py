from dal import autocomplete

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from .models import Karyawan, Karir
from django.contrib.auth.models import User
from akun.models import Profil
from .forms import KaryawanForm, KarirForm


def KaryawanAutocomplete(request):
    if 'term' in request.GET:
        qs = User.objects.filter(username__icontains=request.GET.get('term'))
        # print(qs)
        names = list()
        for profil in qs:
            # names.append(profil.id)
            names.append(profil.username)
        return JsonResponse(names, safe=False)


def index(request):

    cuser = request.user
    admin = User.objects.filter(username=cuser, is_superuser=True)
    
    if admin:
        datas = Karyawan.objects.all().order_by('karyawan__user')
    else:
        datas = Karyawan.objects.select_related('karyawan__user').filter(karyawan__user__username=cuser)

    return render(request,'human_capital/karyawan/karyawan.html', {'datas':datas, 'cuser':cuser})

def hapus_k(request, pk):
    data_k = get_object_or_404(Karyawan, pk=pk)
    if data_k.gambar:
        data_k.gambar.delete()
    data_k.delete()
    return redirect('home:hcp')

def edit_k(request, pk):
    data_k = get_object_or_404(Karyawan, pk=pk)
    if request.method == 'POST':
        form = KaryawanForm(request.POST, request.FILES, instance=data_k)
        if form.is_valid():
            data_k = form.save(commit=False)
            data_k.save()
            return redirect('hcp:home')
    else:
        form = KaryawanForm(instance=data_k)
    return render(request,
                  'human_capital/keluarga/edit_k.html',
                  {'form': form,
                   'data_k': data_k})

def detail_k(request, pk):
    
    data_k = get_object_or_404(Karyawan, pk=pk)
    
    context = {
        # 'gbr': Profil.objects.all(),
        'data_k': data_k,
        
    }
    return render(request, 'human_capital/keluarga/detail_k.html', context)
    
def karir(request):

    cuser = request.user
    
    datas = Karir.objects.select_related('karyawan_k__karyawan__user').filter(karyawan_k__karyawan__user__username=cuser)
    
    context = {
        'cuser':cuser,
        'datas': datas,
       }
    return render(request,'human_capital/karir.html', context)

def tambah_karir(request):
    # cuser = request.user
    # kar = get_object_or_404(Karyawan, pk=pk)
    if request.method == 'POST':
        form = KarirForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            # post['user'] = cuser
            post.save()
            return redirect('hcp:karir')
    else:
        form = KarirForm()
    return render(request,'human_capital/tambah_karir.html', {'form':form})

def tambah_k(request):
    # reqs = request.POST.get('karyawan')
    # print(q)
    if request.method == 'POST':
        form = KaryawanForm(request.POST)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('hcp:home')
    else:
        form = KaryawanForm()
        
    return render(request,'human_capital/karyawan/tambah_k.html',{'form':form})

class UserAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Profil.objects.none()

        data_user = Profil.objects.all()

        if self.q:
            data_user = data_user.filter(nama__icontains=self.q).order_by('id')
            # data_user = data_user.filter(full_name__icontains=self.q)
        return data_user 
