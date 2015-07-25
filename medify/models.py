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
	
	

	
	
	
