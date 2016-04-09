from django.db import models
from django.utils import timezone
#from datetime import datetime
from django.contrib import admin
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from .slug_snippet import unique_slugify
# class Gener(models.Model):
#     name = models.CharField('gener', max_length=50, blank=True, null=True)
#     desccription = models.CharField('gener description', max_length=200, blank=True, null=True)
#     timestamp = models.DateTimeField(auto_now_add=True, auto_now=False) # Creation time
#     update = models.DateTimeField(auto_now_add=False, auto_now=True) # Update time
#     def __str__(self):
#         return self.name

# class Occupation(models.Model):
#     title = models.CharField('title', max_length=200, unique=True)
#     description = models.TextField('description', blank=True, null=True)
#     def __str__(self):
#         return self.title

# class Person(models.Model):
#     id = models.AutoField(primary_key=True)
#     fullname = models.CharField('Full name', max_length=200 , unique=True)
#     firstname = models.CharField('first name', max_length=200)
#     lastname = models.CharField('last name', max_length=200)
#     gender_list = (('M', 'Male'), ('F', 'Female'))
#     gender = models.CharField(max_length=1, choices=gender_list, blank=True, null=True)
#     age = models.PositiveIntegerField(blank=True, null=True)
#     occupations = models.ManyToManyField(Occupation)
#     nationality = models.CharField(max_length=200, blank=True, null=True)
#     date_of_birth = models.DateField(blank=True, null=True)
#     date_of_death = models.DateField(blank=True, null=True)
#     place_of_birth = models.CharField(max_length=200, blank=True, null=True)
#     place_of_death = models.CharField(max_length=200, blank=True, null=True)
#     wikiPediaPage_ID = models.CharField(max_length=200, blank=True, null=True)
#     biography = models.TextField(blank=True, null=True)
#     timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
#     update = models.DateTimeField(auto_now_add=False, auto_now=True)
#     def __str__(self):
#         #fullname = self.firstname + " " + self.lastname
#         return self.fullname
    

# class Director(models.Model):
#   name = models.CharField('first name', max_length=200)

#   director =  
#   timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
#   update = models.DateTimeField(auto_now_add=False, auto_now=True)
#   def __str__(self):
#       fullname = self.firstname + " " + self.lastname
#       return fullname

# class Writer(models.Model):
#   firstname = models.CharField('first name', max_length=200)
#   lastname = models.CharField('last name', max_length=200)
#   gender_list = (('M', 'Male'), ('F', 'Female'))
#   gender = models.CharField(max_length=1, choices=gender_list)
#   age = models.PositiveIntegerField(blank=True, null=True)
#   date_of_birth = models.DateField(blank=True, null=True)
#   date_of_death = models.DateField(blank=True, null=True)
#   place_of_birth = models.CharField(max_length=200, blank=True, null=True)
#   place_of_death = models.CharField(max_length=200, blank=True, null=True)
#   biography = models.TextField(blank=True, null=True)
#   timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
#   update = models.DateTimeField(auto_now_add=False, auto_now=True)
#   def __str__(self):
#       fullname = self.firstname + " " + self.lastname
#       return fullname

# class Movie(models.Model):
#     id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=200, unique=True)
#     default = timezone.localtime(timezone.now()).year
#     pub_date = models.DateField( blank=True, null=True)
#     geners = models.ManyToManyField(Gener)
#     directors = models.ManyToManyField(Person, related_name="directors")
#     writers = models.ManyToManyField(Person, related_name="writers")
#     actors = models.ManyToManyField(Person, related_name="actors")
#     screenplays = models.ManyToManyField(Person, related_name="screenplays")
#     producers = models.ManyToManyField(Person, related_name="produers")
#     editing = models.ManyToManyField(Person, related_name="editing")
#     cinematography = models.ManyToManyField(Person, related_name="cinematography")
#     musicComposers  = models.ManyToManyField(Person, related_name="musicComposer")
#     wikiPageUrl = models.CharField(max_length=300, blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
#     update = models.DateTimeField(auto_now_add=False, auto_now=True)
#     def __str__(self):
#         return self.title
#     class Meta:
#         ordering = ('title',)

    
class Person(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField('Full name', max_length=200 , unique=True)
    firstname = models.CharField('first name', max_length=200)
    lastname = models.CharField('last name', max_length=200)
    gender_list = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField(max_length=1, choices=gender_list, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    nationality = models.CharField(max_length=200, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)
    place_of_birth = models.CharField(max_length=200, blank=True, null=True)
    place_of_death = models.CharField(max_length=200, blank=True, null=True)
    wikiPediaPage_ID = models.CharField(max_length=200, blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)
    slug = models.SlugField(unique=True)
    def __str__(self):
        #fullname = self.firstname + " " + self.lastname
        return self.fullname
    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.fullname)
            unique_slugify(self, self.slug) 
        super(Person, self).save(*args, **kwargs)

class Gener(models.Model):
    title = models.CharField('gener', max_length=50, blank=True, null=True)
    desccription = models.CharField('gener description', max_length=200, blank=True, null=True)
    def __str__(self):
        return self.title

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('title', max_length=200, unique=True)
    staff = models.ManyToManyField('Person', through='WorkedOn')
    gener = models.ManyToManyField('Gener', related_name='movieGener')
    pub_date = models.DateField( blank=True, null=True)
    wikiPageUrl = models.CharField(max_length=300, blank=True, null=True, verbose_name='wikipedia page')
    slug = models.SlugField(unique=True)
    likes = models.ManyToManyField(User, blank= True, related_name='movieLikes')
    description = models.TextField('description', blank=True, null=True)
    def __str__(self):
        return self.title

    @property
    def total_likes(self):
        """
        Likes for the Movie
        :return: Integer: Likes for the Movie
        """
        return self.likes.count()

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)
            unique_slugify(self, self.slug) 
        super(Movie, self).save(*args, **kwargs)

# model in case you want to specify anything specific for roles for every person
class Role(models.Model):
    title = models.CharField('title', max_length=200, unique=True)
    description = models.TextField('description', blank=True, null=True)
    def __str__(self):
        return self.title

# can have extra fields, e.g. dates worked, pay, etc.
class WorkedOn(models.Model):
    person = models.ForeignKey('Person')
    movie = models.ForeignKey('Movie')
    role = models.ForeignKey('Role')

# RATE_CHOICES = zip( range(1,5), range(1,5) )
class Rating(models.Model):
    user = models.ForeignKey(User , related_name='movieUserRating')
    movie = models.ForeignKey(Movie)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    # timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    # update = models.DateTimeField(auto_now_add=False, auto_now=True)

    # def __str__(self):
    #     return "{} rating {} {}".format(self.user,  self.rating)






