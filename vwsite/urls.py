from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login,name="show_site"),
    path('resetpassword',views.reset,name="reset")
]