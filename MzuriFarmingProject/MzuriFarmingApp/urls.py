from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('farmers/', views.farmers_list, name='farmers_list'),
    path('crops/', views.crops_list, name='crops_list'),
    path('subscriptions/', views.subscriptions_list, name='subscriptions_list'),
    path('reports/', views.reports_list, name='reports_list'),
    path('consulting_requests/', views.consulting_requests_list, name='consulting_requests_list'),
]