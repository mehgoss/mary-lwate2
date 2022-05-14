from django import views
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404

urlpatterns = [
    path('', views.Home, name='home'),
    path('awards/', views.Award_cert, name='awards'),
    path('services/', views.Service_re, name='services'),
    path('contact/', views.contact, name='contact'),
    path('cover/', views.cover, name='cover'),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'myapp.views.error_404_handler'