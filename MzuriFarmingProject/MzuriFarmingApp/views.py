from django.shortcuts import render, redirect, get_object_or_404
from .models import Farmers, Crops, Subscriptions, Reports, ConsultingRequests
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import LoginForm, RegistrationForm, CropForm

def index(request):
    return render(request, 'index.html')

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
                return redirect('crops_list')  # Redirect to a homepage or dashboard
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # Create a new user
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')  # Redirect to login page
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

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
