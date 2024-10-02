
from django.contrib import admin
from django.urls import include, path
from board_varification import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.qrscanner, name='qrcode_scan'),
    #path('verify-qr-code/', views.verify_qr_code, name='verify_qr_code'),
    path('board_varification/', include('board_varification.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)