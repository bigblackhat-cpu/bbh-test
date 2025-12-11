from django.db import models

# Create your models here.
class HouseRent(models.Model):
    id = models.BigIntegerField(blank=True, null=False,primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    community_name = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    rent = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    layout = models.CharField(max_length=255, blank=True, null=True)
    listing_update_time = models.CharField(max_length=255, blank=True, null=True)
    lianjia_complaint_phone = models.CharField(max_length=255, blank=True, null=True)
    property_verification_id = models.CharField(max_length=255, blank=True, null=True)
    rental_type = models.CharField(max_length=255, blank=True, null=True)
    property_type = models.CharField(max_length=255, blank=True, null=True)
    floor_info = models.CharField(max_length=255, blank=True, null=True)
    orientation_floor_type = models.CharField(max_length=255, blank=True, null=True)
    additional_info = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    agent = models.CharField(max_length=255, blank=True, null=True)
    tag = models.CharField(max_length=255, blank=True, null=True)
    area_sqm = models.CharField(max_length=255, blank=True, null=True)
    orientation = models.CharField(max_length=255, blank=True, null=True)
    maintenance = models.CharField(max_length=255, blank=True, null=True)
    move_in_date = models.CharField(max_length=255, blank=True, null=True)
    has_elevator = models.CharField(max_length=255, blank=True, null=True)
    parking = models.CharField(max_length=255, blank=True, null=True)
    water_usage = models.CharField(max_length=255, blank=True, null=True)
    electricity_usage = models.CharField(max_length=255, blank=True, null=True)
    has_gas = models.CharField(max_length=255, blank=True, null=True)
    heating = models.CharField(max_length=255, blank=True, null=True)
    lease_term = models.CharField(max_length=255, blank=True, null=True)
    viewing_availability = models.CharField(max_length=255, blank=True, null=True)
    payment_method = models.CharField(max_length=255, blank=True, null=True)
    monthly_rent_cny = models.IntegerField(blank=True, null=True)
    deposit_cny = models.IntegerField(blank=True, null=True)
    service_fee = models.CharField(max_length=255, blank=True, null=True)
    agency_fee_cny = models.CharField(max_length=255, blank=True, null=True)
    distance_to_transport_m = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(null=False)

    class Meta:
        managed = False
        db_table = 'house_rent'


class PatientData(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    has_eye_disease = models.CharField(max_length=255, blank=True, null=True)
    has_diabetic_retinopathy = models.CharField(max_length=255, blank=True, null=True)
    sugar_percentage = models.FloatField(blank=True, null=True)
    glucose_percentage = models.FloatField(blank=True, null=True)
    cholesterol_percentage = models.FloatField(blank=True, null=True)
    obesity_percentage = models.FloatField(blank=True, null=True)
    blood_pressure = models.CharField(max_length=255, blank=True, null=True)
    heart_rate = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_data'


class Results(models.Model):
    race_id = models.CharField(max_length=255, blank=True, null=True)
    driver_id = models.CharField(max_length=255, blank=True, null=True)
    constructor_id = models.CharField(max_length=255, blank=True, null=True)
    grid = models.IntegerField(blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    position_order = models.IntegerField(blank=True, null=True)
    points = models.FloatField(blank=True, null=True)
    laps = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'results'