"""
URL configuration for bank_account_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from account import views


app_name="account"

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name="home"),

    # path('createacc',views.createacc,name="createacc"),
    #
    # path('detail/<int:n>',views.detail,name="detail"),

    path('reg/',views.register,name="register"),

    path('log/',views.user_login,name="login"),

    path('logout/', views.user_logout, name="user_logout"),

    path('viewtransaction/', views.viewtransaction, name="viewtransaction"),

    path('create/', views.create, name="create"),

    path('update/', views.update, name="update"),

    path('edit/<int:n>', views.edit, name="edit"),

    path('delete/<int:n>', views.delete, name="delete"),

]
