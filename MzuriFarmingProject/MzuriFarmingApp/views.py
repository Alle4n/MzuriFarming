from django.shortcuts import render, redirect, get_object_or_404
from .models import Farmers, Crops, Subscriptions, Reports, ConsultingRequests
from .forms import CropForm, UserForm 

def index(request):
    return render(request, 'index.html')

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/crops')
    else:
        form = UserForm()

    return render(request, 'users.html', {'form': form})

        
def farmers_list(request):
    farmers = Farmers.objects.all()
    return render(request, 'farmers.html', {'farmers': farmers})

def crops_list(request):
    crops = Crops.objects.all()

    if request.method == 'POST':
        if 'add_crop' in request.POST:
            form = CropForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('crops_list')
        
        elif 'edit_crop' in request.POST:
            crop_id = request.POST.get('crop_id')
            crop = get_object_or_404(Crops, id=crop_id)
            form = CropForm(request.POST, instance=crop)
            if form.is_valid():
                form.save()
                return redirect('crops_list')

        elif 'delete_crop' in request.POST:
            crop_id = request.POST.get('crop_id')
            crop = get_object_or_404(Crops, id=crop_id)
            crop.delete()
            return redirect('crops_list')
    else:
        form = CropForm()

    return render(request, 'crops.html', {'crops': crops, 'form': form})

def subscriptions_list(request):
    subscriptions = Subscriptions.objects.all()
    return render(request, 'subscriptions.html', {'subscriptions': subscriptions})

def reports_list(request):
    reports = Reports.objects.all()
    return render(request, 'reports.html', {'reports': reports})

def consulting_requests_list(request):
    requests = ConsultingRequests.objects.all()
    return render(request, 'consulting_requests.html', {'requests': requests})
