from django.urls import path
from .  import  views

urlpatterns = [
    path('', views.home, name='home'),
    path('jamiyat-tarixi/', views.jamiyat_tarixi, name="jamiyat_tarixi"),
    path('jamiyat-bugun/', views.jamiyat_bugun, name="jamiyat_bugun"),
    path('raxbar/', views.raxbar, name="raxbar"),
    path('ish/', views.ish, name="ish"),
    path('strategiya/', views.strategiya, name="strategiya"),
    path('horij/', views.horij, name="horij"),
    path('xizmat/', views.maxsulot, name="xizmat"),
    path('tuzulma/', views.tuzulma, name="tuzulma"),
    path('reja/', views.reja, name="reja"),
    path('strategy/', views.strategy, name="strategy"),
    path('nizom/', views.nizom, name="nizom"),
    path('korporativ/<int:pk>/', views.korporative_detail, name="korpo_detail"),
    path('intraktiv/', views.intrak, name="intraktiv")
]