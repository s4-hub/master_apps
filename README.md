# master_apps
Master apps

Depedencies :
Python3.7, Virtual Enviroments, PIP

How to :
- Setelah selesai virtual environments, crate venv : $ python3.7 -m venv my_env (di windows sama perintahnya)
- Pindah ke direktori dan ketik : $ source my_env/bin/activate atau C:\my_env>Scripts\activate
- clone aplikasinya
- pindah ke direktori aplikasi
- jalankan perintah : pip install -r requirements.txt dan tunggu hingga selesai.
- kemudian jalankan : python manage.py makemigrations (mengcretae database), python manage.py migrate(commit)
- create user dengan perintah : python manage.py createsuperuser
- running kn server dengan perintah : python manage.py runserver
- akses alamat di localhost:8000
