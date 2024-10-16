from django.urls import path, include
from . import views 



urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('farmers/', views.farmers_list, name='farmers_list'),
    path('crops/', views.crops_list, name='crops_list'),
    path('subscriptions/', views.subscriptions_list, name='subscriptions_list'),
    path('reports/', views.reports_list, name='reports_list'),
    path('consulting_requests/', views.consulting_requests_list, name='consulting_requests_list'),
     path('dashboard/', views.dashboard, name='dashboard'),
]