from django.shortcuts import render
from django.http import HttpResponse
from .forms import MovieForm ,ActorForm

from .models import Movie

# Create your views here.
def index(request):
    data = {"title":"Movie part of the web site!"}
    return render(request, 'movies/index.html', data)

def addPerson(request):
	
	form = ActorForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	context = {
		"title":"Add Person",
		"form":form
	}
	return render(request, 'movies/addperson.html', context)



def addMovie(request):
	
	form = MovieForm()
	context = {
		"title":"Add Movie",
		"form":form
	}
	return render(request, 'movies/addmovie.html', context)

