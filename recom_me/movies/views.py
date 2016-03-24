from django.shortcuts import render
from django.http import HttpResponse
from .forms import MovieForm ,PersonForm

#from .models import Movie, Person, Gener, Occupation
from .models import Movie, Person
import pickle
# Create your views here.
def index(request):
    data = {"title":"Movie part of the web site!"}
    return render(request, 'movies/index.html', data)

def addPerson(request):
    
    form = PersonForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        #data = instance.cleaned_data
        instance.fullname = instance.firstname + ' '+ instance.lastname
        #data['fullname'] = data['firstname'] + " " + data['lastname']
        print(instance)
        # occupations = self.cleaned_data.get('occupations', None)
        # if occupations is not None:
        #     for occupation in occupations.split(","):
        #         occ = Occupation.objects.create(name = occupation)
        #         instance.title.add(occ)
        instance.save()
    context = {
        "title":"Add Person",
        "form":form
    }
    return render(request, 'movies/addperson.html', context)



def addMovie(request):
    
    form = MovieForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        #data = instance.cleaned_data
        
        #data['fullname'] = data['firstname'] + " " + data['lastname']
        print(form.cleaned_data)
        # occupations = self.cleaned_data.get('occupations', None)
        # if occupations is not None:
        #     for occupation in occupations.split(","):
        #         occ = Occupation.objects.create(name = occupation)
        #         instance.title.add(occ)
        #instance.save()
    context = {
        "title":"Add Movie",
        "form":form
    }
    return render(request, 'movies/addmovie.html', context)

