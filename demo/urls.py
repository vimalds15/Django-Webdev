from django.urls import path
from . import views
from demo import models
from django.conf import settings
from django.conf.urls.static import static

app_name="demo"
urlpatterns = [
    path('',views.index,name="indexpage"),
    path('demo/rightcont/',views.index,name="home"),
    path('demo/javascript/',views.javascript,name="javascript"),
    path('demo/python/',views.python,name="python"),
    path('demo/java/',views.java,name="java"),
    path('demo/kotlin/',views.kotlin,name="kotlin"),
    path('demo/cpp/',views.cpp,name="cpp"),
]
