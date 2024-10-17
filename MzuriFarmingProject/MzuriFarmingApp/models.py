from django.db import models
from django.utils import timezone
from decimal import Decimal

class Users(models.Model):
    USER_ROLES = (
        ('Farmer', 'Farmer'),
        ('Agronomist', 'Agronomist'),
        ('Researcher', 'Researcher'),
        ('Admin', 'Admin'),
    )
    
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=64)  # Consider using a hashed password
    email = models.EmailField(max_length=100, unique=True)
    role = models.CharField(max_length=15, choices=USER_ROLES)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username

class Farmers(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, related_name='farmer_profile')
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=255)
    farm_size = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.full_name

class Crops(models.Model):
    crop_name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    average_yield = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # to be calculated
    classification = models.CharField(max_length=100)  
    harvest_in_kg = models.DecimalField(max_digits=15, decimal_places=2)
    land_size_acres = models.DecimalField(max_digits=10, decimal_places=2)

    def calculate_average_yield(self):
        if self.land_size_acres > 0:  # Prevent division by zero
            return Decimal(self.harvest_in_kg) / Decimal(self.land_size_acres) * Decimal('2.47105')  # Use Decimal for conversion
        return Decimal('0')  # Return a Decimal zero

    def save(self, *args, **kwargs):
        self.average_yield = self.calculate_average_yield()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.crop_name

class WeatherData(models.Model):
    location = models.CharField(max_length=255)
    date = models.DateField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    rainfall = models.DecimalField(max_digits=5, decimal_places=2)
    weather_condition = models.CharField(max_length=100)

    class Meta:
        unique_together = ('location', 'date')

    def __str__(self):
        return f"{self.date} - {self.location}"

class SoilConditions(models.Model):
    location = models.CharField(max_length=255)
    ph = models.DecimalField(max_digits=4, decimal_places=2)
    organic_matter = models.DecimalField(max_digits=5, decimal_places=2)
    nitrogen = models.DecimalField(max_digits=5, decimal_places=2)
    phosphorus = models.DecimalField(max_digits=5, decimal_places=2)
    potassium = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        unique_together = ('location', 'ph')

    def __str__(self):
        return self.location

class CropYield(models.Model):
    farmer = models.ForeignKey(Farmers, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crops, on_delete=models.CASCADE)
    year = models.IntegerField()
    yield_value = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('farmer', 'crop', 'year')

    def __str__(self):
        return f"{self.crop} - {self.year}"

class Subscriptions(models.Model):
    PLAN_CHOICES = (
        ('Basic', 'Basic'),
        ('Standard', 'Standard'),
        ('Professional', 'Professional'),
    )
    
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    plan = models.CharField(max_length=15, choices=PLAN_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user} - {self.plan}"

class Reports(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    report_type = models.CharField(max_length=15)
    generated_at = models.DateTimeField(auto_now_add=True)
    report_data = models.TextField()

    def __str__(self):
        return f"{self.report_type} - {self.generated_at}"

class ConsultingRequests(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15)
    description = models.TextField()

    def __str__(self):
        return f"Request by {self.user} on {self.request_date}"
