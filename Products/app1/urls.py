from django.urls import path
from app1 import views

urlpatterns=[
    path('mobiles/<int:pid>',views.msearch,name="ms"),
    path('laptops/<int:pid>',views.lsearch,name="ls"),
    path('airpods/<int:pid>',views.asearch,name='As')
]