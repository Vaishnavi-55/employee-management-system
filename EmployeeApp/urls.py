from django.urls import path
from . import views
app_name='super'
urlpatterns = [path('signup/',views.signup,name="signup.url"),
    path('login/',views.Login,name="login.url"),
    path('logout/',views.Logout,name='logout.url')
    ]