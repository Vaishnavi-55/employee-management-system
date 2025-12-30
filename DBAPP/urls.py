from django.urls import path
from . import views

app_name = 'DBAPP'
urlpatterns=[path('insert/',views.insert,name='insert.url'),
             path('showdetails/',views.show,name='showdetails.url'),
             path('update/<int:eno>/',views.update,name='update.urls'),
             path('delete/<int:eno>/',views.delete,name='delete.url'),
             path('all/',views.details,name='super.url')
             ]