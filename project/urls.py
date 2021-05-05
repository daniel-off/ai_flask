from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name="index"),
    path('upload', views.image_upload, name='upload'),
    path('logins',views.logins, name='Logins'),
    path('join',views.join,name='join'),
    path('register', views.register, name='register'),
]