from django.contrib import admin
from django.urls import path
from holidays import views
urlpatterns = [
    path('', views.index,name="home"),
    path("st_tour/<package_name>/",views.packageinfo,name="packageinfo"),
    path("contact-us/",views.contactpage,name="contactpage"),
    path("category/blog/",views.blogs,name="blogs"),
        
]

