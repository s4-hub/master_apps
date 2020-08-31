from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
# from django.core.files.storage import FileSystemStorage

from .models import Antol
from .forms import TemplateForm
import PyPDF2 as pypdf
import csv
import io
import six
from tabula import convert_into


# Create your views here.
def manual_replace(s, char, index):
    return s[:index]+char+s[index+1:]

def index(request):
    datas = Antol.objects.all()
    context = {
        'datas': datas

    }
    return render(request, 'antol/index.html', context)


def csv_to_models(request):
    # datas = Antol.objects.all()
    datas = 'Harus sesuai format'
    if request.method == 'GET':
        return render(request, 'antol/upload.html', {'datas': datas})
    csv_file = request.FILES['file']
    print(csv_file.size)
    tgl = request.POST['tgl']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'File harus format CSV')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    for column in csv.reader(io_string, delimiter=','):

        _,  created = Antol.objects.update_or_create(
            kode=column[1],
            kpj=column[2],
            nik=column[3],
            nama=column[4],
            email=column[5],
            no_hp=column[6],
            shift=column[7],
            kegiatan=column[8],
            tgl_antol=tgl
        )

    context = {}
    return render(request, 'antol/upload.html', context)


def simpan(request):
    if request.method == 'GET':
        return render(request, 'antol/upload.html')

    pdf_file = request.FILES['file']
    tgl = request.POST['tgl']
    if not pdf_file.name.endswith('.pdf'):
        messages.error(request, 'Harus format PDF')

    if pdf_file.size < 5242880:
        convert_into(pdf_file, "data.csv",
                     output_format='csv')
        with open('data.csv', 'rb') as csv_file:

            next(csv_file)

            io_string = io.TextIOWrapper(csv_file, encoding='utf-8')

            for column in csv.reader(io_string, delimiter=','):
                # print(column[0])
                _,  created = Antol.objects.update_or_create(
                    kode=column[1],
                    kpj=column[2],
                    nik=column[3],
                    nama=column[4],
                    no_hp=column[5],
                    email=column[6],
                    shift=column[7],
                    kegiatan=column[8],
                    tgl_antol=tgl
                )

    else:
        messages.error(request, 'Ukuran file harus <= 5MB')
        return render(request, 'antol/upload.html')
  
    context = {}
    return render(request, 'antol/upload.html', context)

def template_pesan(request):
    
    if request.method == 'POST':
        form = TemplateForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            return redirect('antol:home')
    else:
        form = TemplateForm()
    return render(request, 'antol/template.html', {'form':form})

def send_wa(request, pk):
    data_k = get_object_or_404(Antol, pk=pk)

    pesan = """Yth. bpk/ibu {}. %0A%0ASaat ini kami hanya ingin menginformasikan bahwasannya akan ada petugas kami yang akan menghubungi bpk/ibu baik melalui video call atau pun telepon untuk mengkorfimasi terhadap pengajuan Klaim JHT yang sebelumnya bpk/ibu ajukan secara online.%0ADiharapkan kpd bpk/ibu menyiapkan berkas-berkas berupa *KTP, KK, Parklaring, KPJ dan buku tabungan*.
            %0A%0ATerima Kasih.""".format(data_k.nama)
    pesan2 = request.POST.get('textarea-input')
    
    no = manual_replace(data_k.email,'62',0)
    context = {
        'data_k':data_k,
        'pesan':pesan,
        'no':no
    }

    return render(request, 'antol/sent_wa.html', context)
