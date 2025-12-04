"""
URL configuration for medicalstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from store import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup_page, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('create/', views.create_medicine, name='createproduct'),
    path('retrieve/', views.retrieve_medicine, name='retrieveproduct'),
    path('update/<int:id>/', views.update_medicine, name='update'),
    path('delete/<int:id>/', views.delete_medicine, name='delete'),
    path('listing/', views.listing, name='medicine_listing'),
    path('search/', views.search_medicine, name='searchmedicine'),
]
