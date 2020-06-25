from django.shortcuts import render, redirect


from .models import Karyawan, Keluarga, Karir
from .forms import KaryawanForm, KeluargaForm, KarirForm


def index(request):

    cuser = request.user
    datas = Keluarga.objects.all()

    return render(request,'hcp/index.html', {'datas':datas, 'cuser':cuser})

def karir(request):

    datas = Karir.objects.all()
    return render(request,'hcp/karir.html', {'datas':datas})

def tambah_k(request):
    if request.method == 'POST':
        form = KaryawanForm(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.save()

            return redirect('hcp:home')
    else:
        form = KaryawanForm()
    return render(request,'hcp/tambah.html',{'form':form})

