from django.shortcuts import render, redirect
# from datetime import datetime
from django.http import HttpResponse, JsonResponse

import xlwt, datetime

from .models import Aset_IT, Pemeliharaan_Umum, Pemeliharaan_Hardware, Pemeliharaan_Software, Pemeliharaan_Keamanaan, Operator
from .forms import AsetForms, UmumForm, HardwareForm, SoftwareForm, KeamananForm, OperatorForm

def index(request):

    assets = Aset_IT.objects.all()
    context = {
        'assets':assets
    }
    return render(request,'inventaris_apps/index.html',context)

def input_aset(request):
    # datas = Aset_IT.objects.filter(timestamp=datetime.today())
    if request.method == 'POST':
        form = AsetForms(request.POST)
        form2 = UmumForm(request.POST)
        form3 = KeamananForm(request.POST)
        form4 = SoftwareForm(request.POST)
        form5 = HardwareForm(request.POST)
        form6 = OperatorForm(request.POST)
        if form.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid() and form6.is_valid():
            post6 = form6.save(commit=False)
            post6.save()

            post5 = form5.save(commit=False)
            post5.save()

            post4 = form4.save(commit=False)
            post4.save()

            post3 = form3.save(commit=False)
            post3.save()

            post2 = form2.save(commit=False)
            post2.save()

            post = form.save(commit=False)
            post.pemeliharaan_umum = post2
            post.pemeliharaan_keamanan = post3
            post.pemeliharaan_software = post4
            post.pemeliharaan_hardware = post5
            post.operator = post6
            post.save()
            
            return redirect('aset:home')

    else:
        form = AsetForms()
        form2 = UmumForm()
        form3 = KeamananForm()
        form4 = SoftwareForm()
        form5 = HardwareForm()
        form6 = OperatorForm()
    context = {
        'form':form,'form2':form2,
        'form3':form3,'form4':form4,
        'form5':form5,'form6':form6
    }

    return render(request,'inventaris_apps/tambah.html',context)

def export_xls(request):
    response = HttpResponse(content_type='text/ms-excel')
    tgl = datetime.datetime.now().strftime("%d-%m-%Y")
    response['Content-Disposition'] = 'attachment; filename="LAPORAN_ASET_IT_KACAB_LANGSA_{}.xls"'.format(tgl)

    wb = xlwt.Workbook(encoding='utf-8')
    # tgl = datetime.datetime.now().strftime("%d-%m-%Y")
    ws = wb.add_sheet('Laporan Aset IT')
    
    # ws.write_merge(3,6,6,8,'No Registrasi')
    style1 = xlwt.easyxf(num_format_str='DD-MM-YYYY')

    row_num = 1
    
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = [
        'NO REGISTER','PENGGUNA','BIDANG/BAGIAN','JENIS ASET',
        'MERK/TYPE','SERIAL NUMBER','TAHUN PENGADAAN','IP ADDRESS',
        'SISTEM OPERASI','LISENSI OS','OFFICE','LISENSI OFFICE',
        'OCS INVENTORY','ANTIVIRUS','UPDATED',
        'SUDAH MAINTENANCE','MAINTENANCE BERIKUTNYA'
    ]

    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)

    font_style = xlwt.XFStyle()
        
    rows = Aset_IT.objects.all().values_list(
        'no_reg','nama_user__nama','bidang__nama','jenis_aset__nama','merk_type',
        'serial_num','tahun_pengadaan','ip_addr','operasi_sistem__nama','lisensi_os',
        'office__nama','lisensi_office','ocs_inventory','antivirus','update','maintenance_done','maintenance_next'  
    )
        
    for row in rows:
        row_num += 1
        
        for col_num in range(len(row)):
            if col_num == 6 or col_num == 15 or col_num == 16:
                ws.write(row_num, col_num, row[col_num], style1)
            elif col_num == 12:
                ws.write(row_num, col_num, 'OCS Installed', style1)
            elif col_num == 13:
                ws.write(row_num, col_num, 'Trend Micro Installed', style1)
            elif col_num == 14:
                ws.write(row_num, col_num, 'Antivirus Updated', style1)
            else:
                ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    return response

def send_json(request):
    
    qs = Aset_IT.objects.all()
    for q in qs:
        data = [
            {
                'no_reg':q.no_reg,
                'nama_user':q.nama_user__nama,
                'bidang':q.bidang,
            }
        ]
        return JsonResponse(data, safe=False)   