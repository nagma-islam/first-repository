from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('addDoctor/',views.addDoctor, name = 'insert'),
    path('delete/<id>/',views.delete, name = 'delete')
]