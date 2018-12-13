from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='Forum-Home'),
    path('new', views.create_forum,name='Create-Forum'),
    path('open/<int:id>/', views.open_forum, name='Open-Forum'),
    
]
