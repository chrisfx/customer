from django.urls import path
from . import views

urlpatterns = [

]

urlpatterns = [
    path('', views.index, name='index'),
    path('customer/', views.CustomerListView.as_view(), name='customers'),
    path('customer/<int:pk>', views.CustomerDetailView.as_view(), name='customer-detail'),
    path('post/new', views.post_new, name='post_new'),
    path(r'^contact/$', views.contact, name='contact'),

]

