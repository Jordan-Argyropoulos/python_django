from django.urls import path
from . import views

urlpatterns = [
    path('infirmiere/', views.infirmiereApi),
    path('infirmiere/([0-9]+)', views.infirmiereApi),

    path('', views.apiSoins, name='apiSoins')
    #path('soin/', views.apiSoins),
    #path('soin/([0-9]+)', views.apiSoins)
]
