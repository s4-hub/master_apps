from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import Daftar_Perusahaan
from winback.models import LokasiPekerjaan

from tabula import convert_into, read_pdf
from decimal import Decimal
import csv, re
import datetime
import io
import pandas as pd


def index(request):
    datas = Daftar_Perusahaan.objects.all()

    return render(request, 'kepesertaan/index.html', {'datas': datas})


def baca_txt(request):
    if request.method == 'GET':
        datas = {}
        return render(request, 'kepesertaan/upload.html', {'datas':datas})

    txt_file = request.FILES['file']
    if not txt_file.name.endswith('.txt'):
        messages.error(request, 'Txt file support Only')

    read_txt = txt_file.read().decode('utf-8')
    x = txt_file.readlines()
    m = read_txt.replace(',','')
    n = m.replace('\t',',')
    io_string = io.StringIO(n)
    # print(len(io_string))
    # next(io_string)
    

    for column in csv.reader(io_string, delimiter=','):
        # print(column[0])
        # for i in range(len(list(csv.reader(io_string)))-1):
            
        #     a = column[i]
        #     print(a)
        # print(type(column[2]))
        # l = str((list(column[3:4])[0]))
        keps = datetime.datetime.strptime(column[3], '%b-%y').date()
        
        # m = str((list(column[7:8])[0]))
        keps_1 = datetime.datetime.strptime(column[7], '%b-%y').date()
        # print(keps_1)
        # d = str((list(column[10:11])[0]))
        kabupaten = LokasiPekerjaan.objects.only('id').get(nama_kota=column[10])
        
        # a = str((list(column[0:1])[0:]))
        # print(column[10])
                           
        _,  create = Daftar_Perusahaan.objects.update_or_create(
                npp = column[0],
                div = column[1],
                nama = column[2],
                blth_keps = keps,
                total_upah = Decimal(column[6]),
                iuran_terakhir_blth = keps_1,
                iuran_terakhir_jlh = Decimal(column[8]),
                alamat = column[9],
                kabupaten = kabupaten,
                nama_pic = column[13],
                jabatan_pic = column[14],
                no_hp_pic = column[15],
                email_pic = column[16]

            )
        # print(str((list(column[3:4])[0])))
        # for kab in kota:
        #     print(kab.id)
    context = {}

    return render(request, 'kepesertaan/upload.html', context)

def baca_csv(request):
    if request.method == 'GET':
        datas = Daftar_Perusahaan.objects.all()
        return render(request, 'kepesertaan/upload.html', {'datas':datas})
    
    # dfs = []
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Only support csv files')

    read_csv = csv_file.read().decode('utf-8')
    # file_list = [line.strip() for line in read_csv]
    datas_csv = pd.read_csv(io.StringIO(read_csv))
    for data in datas_csv:
        print(data.dropna())
    # for data_csv in datas_csv:
    #     print(data_csv)
    
    return render(request, 'kepesertaan/upload.html')

def csv_to_models(request):
    if request.method == 'GET':
        datas = Daftar_Perusahaan.objects.all()
        return render (request, 'kepesertaan/upload.html', {'datas':datas})
    
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Only support CSV')

    read_csv = csv_file.read().decode('utf-8')
    io_string = io.StringIO(read_csv)
    next(io_string)
    # datas_csv = csv.reader(io_string, delimiter=',')
        
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        # print(column[0][:8])
        print(column[:1])
        # for i in range(list(datas_csv)):
        #     print(data_csv[1:i])
                
        # for i in range(len(data_csv)-1):
        #     print(data_csv[i])     
        
        # _,  create = Daftar_Perusahaan.objects.update_or_create(
        #     npp = data_csv[1],
        #     div = data_csv[2],
        #     nama = data_csv[3],

        # )
    return render(request, 'kepesertaan/upload.html')

def upload_pdf(request):
    if request.method == 'GET':
        return render(request, 'kepesertaan/upload.html')

    pdf_file = request.FILES['file']
    if not pdf_file.name.endswith('.pdf'):
        messages.error(request, 'Harus Format PDF')

    pages = read_pdf(pdf_file, pandas_options={'header': None}, pages='all')

    for i in range(len(pages)-1):

        for j in range(len(pages[i][2:])-1):
            k = str((list(pages[i][2:][8]))[j]).replace(',', '')
            if k == 'nan':
                upah = 0
            else:
                upah = Decimal(k)
            l = str((list(pages[i][2:][4]))[j])
            if l == 'nan':
                keps = ' - '
            else:
                keps = datetime.datetime.strptime(l, '%m-%Y').date()
            m = str((list(pages[i][2:][9]))[j])
            if m == 'nan':
                iur_blth == '-'
            else:
                iur_blth = datetime.datetime.strptime(m, '%m-%Y').date()

            n = str((list(pages[i][2:][10]))[j]).replace(',', '')
            if n == 'nan':
                iur_jlh = 0
            else:
                iur_jlh = Decimal(n)
            o = str((list(pages[i][2:][18]))[j])
            
            if o == 'nan':
                email = '-'
            else:
                email = (list(pages[i][2:][18]))
                print(email)
            # _,  created = Daftar_Perusahaan.objects.update_or_create(
            #     npp=(list(pages[i][2:][1]))[j],
            #     div=(list(pages[i][2:][2]))[j],
            #     nama=(list(pages[i][2:][3]))[j],
            #     blth_keps=keps,
            #     total_upah=upah,
            #     iuran_terakhir_blth=iur_blth,
            #     iuran_terakhir_jlh=iur_jlh,
            #     alamat=(list(pages[i][2:][11]))[j],
            #     kabupaten=(list(pages[i][2:][12]))[j],
            #     nama_pic=(list(pages[i][2:][15]))[j],
            #     jabatan_pic=(list(pages[i][2:][16]))[j],
            #     no_hp_pic=(list(pages[i][2:][17]))[j],
            #     email_pic=email

            # )
    context = {}
    return render(request, 'kepesertaan/upload.html', context)

