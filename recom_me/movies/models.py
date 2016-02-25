from django.db import models
from django.utils import timezone
#from datetime import datetime

class Gener(models.Model):
	name = models.CharField('gener', max_length=50)
	desc = models.CharField('gener description', max_length=200, blank=True, null=True)

	def __str__(self):
		return self.name

class Actor(models.Model):
	firstname = models.CharField('first name', max_length=200)
	lastname = models.CharField('last name', max_length=200)
	gender_list = (('M', 'Male'), ('F', 'Female'))
	gender = models.CharField(max_length=1, choices=gender_list)
	date_of_birth = models.DateField(blank=True, null=True)
	date_of_death = models.DateField(blank=True, null=True)
	place_of_birth = models.CharField(max_length=200, blank=True, null=True)
	place_of_death = models.CharField(max_length=200, blank=True, null=True)
	biography = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.lastname

class Director(models.Model):
	firstname = models.CharField('first name', max_length=200)
	lastname = models.CharField('last name', max_length=200)
	gender_list = (('M', 'Male'), ('F', 'Female'))
	gender = models.CharField(max_length=1, choices=gender_list)
	date_of_birth = models.DateField(blank=True, null=True)
	date_of_death = models.DateField(blank=True, null=True)
	place_of_birth = models.CharField(max_length=200, blank=True, null=True)
	place_of_death = models.CharField(max_length=200, blank=True, null=True)
	biography = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.lastname

class Writer(models.Model):
	firstname = models.CharField('first name', max_length=200)
	lastname = models.CharField('last name', max_length=200)
	gender_list = (('M', 'Male'), ('F', 'Female'))
	gender = models.CharField(max_length=1, choices=gender_list)
	date_of_birth = models.DateField(blank=True, null=True)
	date_of_death = models.DateField(blank=True, null=True)
	place_of_birth = models.CharField(max_length=200, blank=True, null=True)
	place_of_death = models.CharField(max_length=200, blank=True, null=True)
	biography = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.lastname

class Movie(models.Model):
	title = models.CharField(max_length=200)
	#default = timezone.localtime(timezone.now()).year
	pub_date = models.DateField(blank=True, null=True)
	geners = models.ManyToManyField(Gener)
	directors = models.ManyToManyField(Director)
	writers = models.ManyToManyField(Writer)
	actors = models.ManyToManyField(Actor)
	description = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.title


