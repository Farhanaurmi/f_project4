"""final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from project import views
from register import views as v
from contact import views as contact_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('project.urls')),
    path('register/', v.register, name='register'),
    path('logout', v.logoutuser, name='logoutuser'),
    path('loginuser', v.loginuser, name='loginuser'),
    path('', views.index, name="home"),
    path('index/', views.index, name="home"),
    path('allarchive', views.allarchive, name="allarchive"),
    path('editproject/<int:pk>', views.editproject, name="editproject"),
    path('deleteproject/<int:pk>', views.deleteproject, name="deleteproject"),
    path('archiveproject/<int:pk>', views.archiveproject, name="archiveproject"),
    path('createproject', views.createproject, name="createproject"),
    path('controlpanel', views.controlpanel, name="controlpanel"),
    path('test/', views.index2, name="test"),
    path('test2/', views.index3, name="test1"),
    path('contact/', views.index4, name="contact"),
    path('about/', views.index5, name="about"),
    path('courses/', views.index6, name="courses"),
    path('contacts/', contact_views.contact_view, name='contact'),
    path('buynow', views.buynow, name='buynow'),
    path('csharp', views.csharp, name='csharp'),
    path('python', views.python, name='python'),
    path('java', views.java, name='java'),
]
