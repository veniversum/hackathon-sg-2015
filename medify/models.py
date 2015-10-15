from django.db import models

# Create your models here.

class ApprovedMedication(models.Model):
	licence_no = models.CharField(max_length=9, unique=True)
	product_name = models.CharField(max_length=100)
	licence_holder = models.CharField(max_length=100)
	approval_date = models.DateField()
	f_class = models.CharField(max_length=50)
	atc_code = models.CharField(max_length=50, blank=True)
	dosage_form = models.CharField(max_length=50)
	route = models.CharField(max_length=50)
	manufacturer = models.CharField(max_length=200)
	country = models.CharField(max_length=50)
	active_ingredients = models.TextField()
	strength = models.TextField()

class ChineseMedication(models.Model):
    product_name = models.CharField(max_length=100)
    brand_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    dosage_form = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=200)
    country = models.CharField(max_length=50)
	
class IllegalMedication(models.Model):
	product_name = models.CharField(max_length=100)
	dosage_form = models.CharField(max_length=50,blank=True)
	dosage_form_shape = models.CharField(max_length=50,blank=True)
	dosage_form_marking = models.CharField(max_length=50,blank=True)
	dosage_form_colour = models.CharField(max_length=50,blank=True)
	adulterant_type = models.CharField(max_length=100,blank=True)
	country = models.CharField(max_length=50,blank=True)
	manufacturer = models.CharField(max_length=200,blank=True)
	remarks = models.TextField(blank=True)
	
class Pharmacy(models.Model):
    pharmacy_name = models.CharField(max_length=100)
    zipcode = models.IntegerField(null=True, blank=True)
    building = models.CharField(max_length=50)
    coords = models.CharField(max_length=50)
    
class ApprovedDevice(models.Model):
	device_name = models.CharField(max_length=200,blank=True)
	description	= models.TextField(blank=True)
	gmdn = models.TextField(blank=True)
	speciality = models.TextField(blank=True)
	hs_code = models.CharField(max_length=50,blank=True)
	hsa_product_code = models.CharField(max_length=50,blank=True)
	medical_device_class = models.CharField(max_length=50,blank=True)
	registration_number = models.CharField(max_length=50,blank=True)
	registration_date = models.DateField()
	change_date = models.CharField(max_length=50,blank=True)
	expiry_date = models.DateField()
	product_owner_name = models.TextField(blank=True)
	product_owner_short_name = models.CharField(max_length=200,blank=True)
	product_owner_address = models.TextField(blank=True)
	registrant_name= models.CharField(max_length=200,blank=True)
	registrant_address = models.TextField(blank=True)
	imported_by_name= models.CharField(max_length=200,blank=True)
	imported_by_address = models.TextField(blank=True)
	models_name= models.TextField(blank=True)
	identifier= models.TextField(blank=True)
