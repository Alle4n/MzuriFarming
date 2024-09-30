from django.db import models

# Create your models here.
class Users(models.Model):
    USER_ROLES = (
        ('Farmer', 'Farmer'),
        ('Agronomist', 'Agronomist'),
        ('Researcher', 'Researcher'),
        ('Admin', 'Admin'),
    )
    
    Username = models.CharField(max_length=50, unique=True)
    PasswordHash = models.CharField(max_length=64)
    Email = models.EmailField(max_length=100, unique=True)
    Role = models.CharField(max_length=15, choices=USER_ROLES)
    CreatedAt = models.DateTimeField(auto_now_add=True)

class Farmers(models.Model):
    User = models.OneToOneField(Users, on_delete=models.CASCADE)
    FullName = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=15)
    Location = models.CharField(max_length=255)
    FarmSize = models.DecimalField(max_digits=10, decimal_places=2)

class Crops(models.Model):
    CropName = models.CharField(max_length=100)
    ScientificName = models.CharField(max_length=100)
    AverageYield = models.DecimalField(max_digits=10, decimal_places=2)

class WeatherData(models.Model):
    Location = models.CharField(max_length=255)
    Date = models.DateField()
    Temperature = models.DecimalField(max_digits=5, decimal_places=2)
    Humidity = models.DecimalField(max_digits=5, decimal_places=2)
    Rainfall = models.DecimalField(max_digits=5, decimal_places=2)
    WeatherCondition = models.CharField(max_length=100)

class SoilConditions(models.Model):
    Location = models.CharField(max_length=255)
    pH = models.DecimalField(max_digits=4, decimal_places=2)
    OrganicMatter = models.DecimalField(max_digits=5, decimal_places=2)
    Nitrogen = models.DecimalField(max_digits=5, decimal_places=2)
    Phosphorus = models.DecimalField(max_digits=5, decimal_places=2)
    Potassium = models.DecimalField(max_digits=5, decimal_places=2)

class CropYield(models.Model):
    Farmer = models.ForeignKey(Farmers, on_delete=models.CASCADE)
    Crop = models.ForeignKey(Crops, on_delete=models.CASCADE)
    Year = models.IntegerField()
    Yield = models.DecimalField(max_digits=10, decimal_places=2)

class Subscriptions(models.Model):
    PLAN_CHOICES = (
        ('Basic', 'Basic'),
        ('Standard', 'Standard'),
        ('Professional', 'Professional'),
    )
    
    User = models.OneToOneField(Users, on_delete=models.CASCADE)
    Plan = models.CharField(max_length=15, choices=PLAN_CHOICES)
    StartDate = models.DateField()
    EndDate = models.DateField()
    Status = models.CharField(max_length=15)

class Reports(models.Model):
    User = models.ForeignKey(Users, on_delete=models.CASCADE)
    ReportType = models.CharField(max_length=15)
    GeneratedAt = models.DateTimeField(auto_now_add=True)
    ReportData = models.TextField()

class ConsultingRequests(models.Model):
    User = models.ForeignKey(Users, on_delete=models.CASCADE)
    RequestDate = models.DateTimeField(auto_now_add=True)
    Status = models.CharField(max_length=15)
    Description = models.TextField()