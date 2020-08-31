from django.shortcuts import render, redirect


from .models import Produk, KategoriProduk, SatuanProduk
from .forms import InputProduk, KategoriProdukForm, SatuanProdukForm

# Create your views here.

def index(request):

    datas = Produk.objects.all()

    context = {
        'datas':datas
    }

    return render(request,'stockopname/index.html',context)

def inputstok(request):
    if request.method == 'POST':
        form = InputProduk(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            return redirect('stockopname:home')
    else:

        form = InputProduk()

        return render(request,'stockopname/input_produk.html',{'form':form})

def inputkategori(request):
    datas = KategoriProduk.objects.all()
    if request.method == 'POST':
        form = KategoriProdukForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            return redirect('stockopname:kategori',{'datas':datas})
    else:
        form = KategoriProdukForm()
        
        return render(request,'stockopname/input_kategori.html',{'form':form,'datas':datas})

def inputsatuan(request):
    datas = SatuanProduk.objects.all()

    if request.method == 'POST':
        form = SatuanProdukForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            return redirect('stockopname:home')

        else:
            form = SatuanProdukForm()

            return render(request,'stockopname/input_satuan.html',{'form':form})

