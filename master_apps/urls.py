from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth_view
# from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('akun.urls')),
    
    path('hcp/', include('human_capital.urls', namespace='hcp')),
    path('stockopname/', include('stockopname.urls', namespace='stockopname')),
    path('antrian/', include('antol.urls')),
    path('winback/',include('winback.urls')),
    path('assets/',include('inventaris_apps.urls', namespace='aset')),
    path('kepesertaan/',include('menu_kepesertaan.urls', namespace='kepesertaaan')),
    path('', views.index, name='home'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns