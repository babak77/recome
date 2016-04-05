from django.shortcuts import render
from django.http import HttpResponse
from .forms import MovieForm ,PersonForm, RatingForm

#from .models import Movie, Person, Gener, Occupation
from .models import Movie, Person, WorkedOn, Role
import pickle

try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


# Create your views here.
@login_required
@require_POST
def like(request):
    if request.method == 'POST':
        user = request.user
        slug = request.POST.get('slug', None)
        movie = get_object_or_404(Movie, slug=slug)

        if movie.likes.filter(id=user.id).exists():
            # user has already liked this movie
            # remove like/user
            movie.likes.remove(user)
            message = 'You disliked this'
        else:
            # add a new like for a movie
            movie.likes.add(user)
            message = 'You liked this'

    ctx = {'likes_count': movie.total_likes, 'message': message }
    print(ctx)
    # use mimetype instead of content_type if django < 5
    return JsonResponse(ctx)
    
def index(request):
    # form = RatingForm(request.POST or None)
    # print(form)
    # if form.is_valid():
    #     instance = form.save(commit=False)
    #     print(instance)
    # data = {"title":"Movie part of the web site!",
    #         "movies" : Movie.objects.all(),
    #         "form":form
    #         }
    
    liked_movies=[]
    movies = Movie.objects.all().order_by('-pub_date')
    user = request.user
    for movie in movies:
        if movie.likes.filter(id=user.id).exists():
            
            liked_movies.append(movie)
    data = {"title":"Movie part of the web site!",
            "movies" : movies,
            "liked_movies" : liked_movies,

            }
    return render(request, 'movies/index.html', data)

def movie_detail(request, **kwargs):
    movie = get_object_or_404(Movie, id=kwargs.get('movie_id'))
    context = {
        "title":"Add Person",
        "movie" : movie,
    }
    return render(request, 'movies/movie_detail.html', context)


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

