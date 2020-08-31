from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.template import RequestContext, Template
from django.contrib.auth.decorators import login_required
from akun.models import Profil


@login_required
def index(request):
    # if request.user.is_superuser or request.user.is_active:
    #     # cuser = request.user
    #     # if cuser.is_superuser:
    #     #     avatar = Profil.objects.none()
    #     # else:
    #     #     avatar = Profil.objects.get(user__username=cuser)

    #     return render(request,'index.html')
    # else:
    #     return redirect('login')
    return render(request,'index.html')

# def photo(request):
#     if not request.user.is_superuser:
#         avatar = Profil.objects.geT(user__username=request.user)
#     else:
#         avatar = {}
#     return render(request,'rightpanel.html', {'a':avatar})
