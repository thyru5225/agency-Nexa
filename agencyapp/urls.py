
from django.contrib import admin
from django.urls import path
from agencyapp import views
urlpatterns = [
    path('admin/', admin.site.urls),

path('', views.index, name='index'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('services/', views.service, name='services'),
    path('starter-page/', views.starter, name='starterpage'),
    path('contact/', views.contact, name='contact'),
]

