"""keywordio_lms URL Configuration

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
from django.urls import path
from lms import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin',views.signin),
    path('signup',views.signup),
    path('Addbook',views.addbook),
    path('showbooks',views.showbooks),
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),
    path('records/', views.recordsofbook),
    path('signout',views.signout),
    path('stud_signup',views.stud_signup),
    path('stud_signin',views.stud_signin),
    path('bookslibrary',views.bookslibrary),
    path('stud_signout',views.stud_signout),
    
]
