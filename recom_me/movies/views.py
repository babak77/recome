from django.shortcuts import render
from django.http import HttpResponse
from .forms import MovieForm ,PersonForm

#from .models import Movie, Person, Gener, Occupation
from .models import Movie, Person, WorkedOn, Role
import pickle
# Create your views here.
def index(request):
    data = {"title":"Movie part of the web site!"}
    print(request.POST)
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
        # === add Movie
        title = form.cleaned_data.get('title', None)
        if not Movie.objects.filter(title__iexact = title).exists():
                movie = Movie(title = title)
                movie.save()
        else: 
            movie = Movie.objects.get(title = title)

        # add Directors
        directors = form.cleaned_data.get('directors', None)
        if directors is not None:
            print(directors)
            for director in directors.split(','):
                director_name = director.strip()
                if Person.objects.filter(fullname__iexact = director_name ).exists():
                    person = Person.objects.filter(fullname__iexact = director_name)[0]
                    role = Role.objects.filter(title__iexact = 'director' )[0]
                    workon = WorkedOn(person = person , movie = movie, role = role )
                    workon.save()

        # add screenpalays
        screenplays = form.cleaned_data.get('screenplays', None)
        if screenplays is not None:
            print(screenplays)
            for screenplay in screenplays.split(','):
                screenplay_name = screenplay.strip()
                if Person.objects.filter(fullname__iexact = screenplay_name ).exists():
                    person = Person.objects.filter(fullname__iexact = screenplay_name )[0]
                    role = Role.objects.filter(title__iexact = 'screenplay' )[0]
                    workon = WorkedOn(person = person , movie = movie, role = role )
                    workon.save()
        # add cinematographys
        cinematographys = form.cleaned_data.get('cinematography', None)
        if cinematographys is not None:
            print(cinematographys)
            for cinematography in cinematographys.split(','):
                cinematography_name = cinematography.strip()
                if Person.objects.filter(fullname__iexact = cinematography_name ).exists():
                    person = Person.objects.filter(fullname__iexact = cinematography_name )[0]
                    role = Role.objects.filter(title__iexact = 'cinematography' )[0]
                    workon = WorkedOn(person = person , movie = movie, role = role )
                    workon.save()
        # add editings
        editings = form.cleaned_data.get('editing', None)
        if editings is not None:
            print(editings)
            for editing in editings.split(','):
                editing_name = editing.strip()
                if Person.objects.filter(fullname__iexact = editing_name ).exists():
                    person = Person.objects.filter(fullname__iexact = editing_name )[0]
                    role = Role.objects.filter(title__iexact = 'editing' )[0]
                    workon = WorkedOn(person = person , movie = movie, role = role )
                    workon.save()
        # add producers
        producers = form.cleaned_data.get('producers', None)
        if producers is not None:
            print(producers)
            for producer in producers.split(','):
                producer_name = producer.strip()
                if Person.objects.filter(fullname__iexact = producer_name ).exists():
                    person = Person.objects.filter(fullname__iexact = producer_name )[0]
                    role = Role.objects.filter(title__iexact = 'producer' )[0]
                    workon = WorkedOn(person = person , movie = movie, role = role )
                    workon.save()
    
        musicComposers = form.cleaned_data.get('musicComposers', None)
        if musicComposers is not None:
            print(musicComposers)
            for musicComposer in musicComposers.split(','):
                musicComposer_name = musicComposer.strip()
                if Person.objects.filter(fullname__iexact = musicComposer_name ).exists():
                    person = Person.objects.filter(fullname__iexact = musicComposer_name)[0]
                    role = Role.objects.filter(title__iexact = 'music' )[0]
                    workon = WorkedOn(person = person , movie = movie, role = role )
                    workon.save()

        writers = form.cleaned_data.get('writers', None)
        if writers is not None:
            print(writers)
            for writer in writers.split(','):
                writer_name = writer.strip()
                if Person.objects.filter(fullname__iexact = writer_name ).exists():
                    person = Person.objects.filter(fullname__iexact = writer_name )[0]
                    role = Role.objects.filter(title__iexact = 'writer' )[0]
                    workon = WorkedOn(person = person , movie = movie, role = role )
                    workon.save()

        actors = form.cleaned_data.get('actors', None)
        if actors is not None:
            print(actors)
            for actor in actors.split(','):
                actor_name = actor.strip()
                if Person.objects.filter(fullname__iexact = actor_name ).exists():
                    person = Person.objects.filter(fullname__iexact = actor_name )[0]
                    role = Role.objects.filter(title__iexact = 'actor' )[0]
                    workon = WorkedOn(person = person , movie = movie, role = role )
                    workon.save()

        # occupations = form.cleaned_data.get('occupations', None)
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

