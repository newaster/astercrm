from django.urls import path
from . import views

urlpatterns = [
    path('addsoftware/', views.addsoftware, name='software-add'),
    path('updatesubscription/<id>/',views.updatesubscription, name='update-subscription'),
    path('sales/',views.sales,name='view-sales')
]