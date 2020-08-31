from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
# from datetime import datetime
from django.conf import settings

import io,csv,xlwt

# Create your views here.
from .forms import JenisForm, LokasiForm, DaftarForm
from .models import LokasiPekerjaan, JenisPekerjaan, daftar

def InputJenis(request):
    if request.method == 'POST':
        form = JenisForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            return redirect('winback:input_jenis')
    else:
        form = JenisForm()
    return render(request,'winback/input_jenis.html',{'form':form})

def InputLokasi(request):
    if request.method == 'POST':
        form = LokasiForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('winback:input_lokasi')
    else:
        form = LokasiForm()
    return render(request,'winback/input_lokasi.html',{'form':form})

def DaftarTK(request):
    
    if request.method == 'POST':
        form = DaftarForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            # cek = request.POST.get('nik')
            post.save()

            return redirect('winback:daftar_tk')
    else:
        form = DaftarForm()
    return render(request,'winback/daftar_tk.html',{'form':form})

def DaftarLokasi(request):
    
    context = {
        'datas':LokasiPekerjaan.objects.all()
    }

    return render(request,'winback/lokasi.html',context)

def DaftarJenis(request):
    context = {
        'datas':JenisPekerjaan.objects.all()
    }

    return render(request,'winback/pekerjaan.html',context)

def ListTK(request):
    datas = daftar.objects.all()

    return render(request,'winback/index.html',{'datas':datas})

def upload_pekerjaan(request):
    datas = JenisPekerjaan.objects.all()
    datas = 'Harus sesuai format'
    if request.method == 'GET':
        return render(request, 'winback/upload_pekerjaan.html', {'datas': datas})
    csv_file = request.FILES['file']
    # print(csv_file.size)
    # tgl = request.POST['tgl']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'File harus format CSV')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    for column in csv.reader(io_string, delimiter=','):

        _,  created = JenisPekerjaan.objects.update_or_create(
            kode=column[0],
            nama_pekerjaan=column[1],
            
        )

    context = {}
    return render(request, 'winback/upload_pekerjaan.html', context)

def upload_lokasi(request):
    datas = LokasiPekerjaan.objects.all()
    datas = 'Harus sesuai format'
    if request.method == 'GET':
        return render(request, 'winback/upload_lokasi.html', {'datas': datas})
    csv_file = request.FILES['file1']
    # print(csv_file.size)
    # tgl = request.POST['tgl']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'File harus format CSV')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    for column in csv.reader(io_string, delimiter=','):

        _,  created = LokasiPekerjaan.objects.update_or_create(
            kode=column[0],
            nama_kota=column[1],
            
        )

    context = {}
    return render(request, 'winback/upload_lokasi.html', context)

def export_xls(request):
    response = HttpResponse(content_type='text/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="TEMPLATE_PENDAFTARAN_BPU_TK_BARU_A0200001_000.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Pendaftaran TK Baru BPU')
    
    ws.write(0,2,'Format: DD-MM-YYYY')
    ws.write(0,3,"FORMAT: Diawali '08'")
    ws.write(0,5,'List Jenis Pekerjaan')
    ws.write(0,6,'List Jenis Pekerjaan')
    ws.write(0,7,'List Lokasi Pekerjaan')
    ws.write(0,9,'List Kode Paket')
    ws.write(0,10,'List Bulan Iuran')

    style1 = xlwt.easyxf(num_format_str='DD-MM-YYYY')

    row_num = 1
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Nomor Identitas*','Nama Lengkap*','Tgl. Lahir*','Handphone*','Email','Jenis Pekerjaan 1*',
                'Jenis Pekerjaan 2','Lokasi Pekerjaan*','Upah*','Kode Paket*','Bulan Iuran*',]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows = daftar.objects.all().values_list('nik','nama','tgl_lahir','no_hp','surel','jenis_pekerjaan__kode',
                                            'jenis_pekerjaan2__kode','lokasi_pekerjaan__kode','upah','kode_paket','kode_iuran')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            if col_num == 2:
                ws.write(row_num, col_num, row[col_num], style1)
            else:
                ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    return response

