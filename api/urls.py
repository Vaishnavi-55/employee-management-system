from django.urls import path,include
# from .views import EmployeeViewSet
from .views import EmployeeCreateView,EmployeeModifyView
from rest_framework.routers import DefaultRouter

#For ModelSetView
# router = DefaultRouter()
# router.register(r'employees',EmployeeViewSet,basename='employee')
# urlpatterns = [path('',include(router.urls))]

#For CBV View
urlpatterns = [path('createemployeeapi/',EmployeeCreateView.as_view(),name='createemployee.url'),
               path('createemployee/<int:pk>/',EmployeeModifyView.as_view(),name="modifyview.url")]
