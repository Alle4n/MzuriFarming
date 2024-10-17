from django.shortcuts import render, redirect, get_object_or_404
from .models import Farmers, Crops, Subscriptions, Reports, ConsultingRequests, CropYield, Users
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import LoginForm, RegistrationForm, CropForm
from django.db.models import Sum, Count
import pandas as pd

def index(request):
    return render(request, 'index.html', {'current_page': 'index'})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('dashboard')
            messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form, 'current_page': 'login'})

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form, 'current_page': 'register'})

def farmers_list(request):
    farmers = Farmers.objects.all()
    return render(request, 'farmers.html', {'farmers': farmers, 'current_page': 'farmers'})

def read_crop_data_from_excel(file_path):
    df = pd.read_excel('MzuriFarmingApp/static/excel/crops.xlsx', sheet_name='Sheet1')
    crop_choices = df[['classification', 'cropName', 'scientificName']].drop_duplicates().to_dict('records')
    return crop_choices

def crops_list(request):
    crops = Crops.objects.all()  
    crop_choices = read_crop_data_from_excel('MzuriFarmingApp/static/excel/crops.xlsx')  
    form = CropForm()

    if request.method == 'POST':
        crop_id = request.POST.get('crop_id')

        if 'add_crop' in request.POST:
            form = CropForm(request.POST)
            if form.is_valid():
                crop = form.save(commit=False)
                # Automatically populate scientific_name and classification from crop_choices
                for choice in crop_choices:
                    if choice['cropName'] == crop.crop_name:
                        crop.scientific_name = choice['scientificName']
                        crop.classification = choice['classification']
                        break
                crop.save()
                messages.success(request, 'Crop added successfully!')
                return redirect('crops_list')
            else:
                messages.error(request, 'Failed to add crop. Please check your input.')


        elif 'edit_crop' in request.POST and crop_id:
            crop = get_object_or_404(Crops, id=crop_id)
            form = CropForm(request.POST, instance=crop)
            if form.is_valid():
                form.save()
                messages.success(request, 'Crop updated successfully!')
                return redirect('crops_list')
            else:
                messages.error(request, 'Failed to update crop. Please check your input.')

        elif 'delete_crop' in request.POST and crop_id:
            crop = get_object_or_404(Crops, id=crop_id)
            crop.delete()
            messages.success(request, 'Crop deleted successfully!')
            return redirect('crops_list')

    return render(request, 'crops.html', {
        'crops': crops,
        'form': form,
        'crop_choices': crop_choices,
        'current_page': 'crops'
    })

def subscriptions_list(request):
    subscriptions = Subscriptions.objects.all()
    return render(request, 'subscriptions.html', {'subscriptions': subscriptions, 'current_page': 'subscriptions'})

def reports_list(request):
    reports = Reports.objects.all()
    return render(request, 'reports.html', {'reports': reports, 'current_page': 'reports'})

def consulting_requests_list(request):
    requests = ConsultingRequests.objects.all()
    return render(request, 'consulting_requests.html', {'requests': requests, 'current_page': 'consulting_requests'})

def dashboard(request):
    user_count = Users.objects.count()
    farmer_count = Farmers.objects.count()
    crop_count = Crops.objects.count()

    # Get crop classification counts
    classification_counts = Crops.objects.values('classification').annotate(count=Count('id'))
    classifications = [item['classification'] for item in classification_counts]
    counts = [item['count'] for item in classification_counts]

    # Get average yields for the crops
    average_yield_data = Crops.objects.values('crop_name').annotate(avg_yield=Count('average_yield'))
    yield_labels = [item['crop_name'] for item in average_yield_data]
    average_yields = [item['avg_yield'] for item in average_yield_data]

    context = {
        'user_count': user_count,
        'farmer_count': farmer_count,
        'crop_count': crop_count,
        'classifications': classifications,
        'counts': counts,
        'yield_labels': yield_labels,
        'average_yields': average_yields,
        'current_page': 'dashboard',
    }

    return render(request, 'dashboard.html', context)