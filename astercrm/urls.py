"""astercrm URL Configuration

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
from . import views

app_name = "astercrm"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('lsa/',views.sadb),
    path('ladmin/',views.admindb),
    path('logout/',views.logout_call),
    path('sales/',views.sales_call),
    path('subscription/',views.subscription_call),
    path('sublist/<id>/',views.sublist_call),
    path('lcadmin/<id>/',views.cadmindb),
    path('csales/<id>/',views.csales_call),
    path('csubscription/<id>/',views.csubscription_call),
    path('csublist/<id>/<id2>/',views.csublist_call),
    path('customer/',views.customer_call),
    path('addsoftware/',views.addsoftware_call),
    path('adduser/',views.adduser_call),
    path('addsubscription/',views.addsubscription_call),
    path('addsales/',views.addsales_call)


]
