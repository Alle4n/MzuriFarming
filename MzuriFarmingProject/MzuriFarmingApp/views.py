from django.shortcuts import render
from .models import Farmers, Crops, Subscriptions, Reports, ConsultingRequests

def index(request):
    return render(request, 'index.html')

def farmers_list(request):
    farmers = Farmers.objects.all()
    return render(request, 'farmers.html', {'farmers': farmers})

def crops_list(request):
    crops = Crops.objects.all()
    return render(request, 'crops.html', {'crops': crops})

def subscriptions_list(request):
    subscriptions = Subscriptions.objects.all()
    return render(request, 'subscriptions.html', {'subscriptions': subscriptions})

def reports_list(request):
    reports = Reports.objects.all()
    return render(request, 'reports.html', {'reports': reports})

def consulting_requests_list(request):
    requests = ConsultingRequests.objects.all()
    return render(request, 'consulting_requests.html', {'requests': requests})
