from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.hello,name='home'),
    path('index/fhlshufe',views.index,name='index'),
    path('buy/<int:pk>/',views.buy,name='buy'),
    path('atc/<int:pk>/',views.atc,name='atc'),
    path('pdf/',views.pdf,name='pdf'),
]