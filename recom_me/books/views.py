from django.shortcuts import render
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from .forms import *
from .models import *


@login_required
@require_POST
def like(request):
    if request.method == 'POST':
        user = request.user
        slug = request.POST.get('slug', None)
        book = get_object_or_404(Book, slug=slug)

        if book.likes.filter(id=user.id).exists():
            # user has already liked this book
            # remove like/user
            book.likes.remove(user)
            message = 'You disliked this'
        else:
            # add a new like for a book
            book.likes.add(user)
            message = 'You liked this'

    ctx = {'likes_count': book.total_likes, 'message': message }
    print(ctx)
    # use mimetype instead of content_type if django < 5
    return JsonResponse(ctx)

def index(request):
        
    liked_books=[]
    book_list = Book.objects.all().order_by('-pub_date')
    query = request.GET.get('query')
    if query:
        book_list = book_list.filter(
            Q(title__icontains=query) |
            Q(Original_title__icontains=query) | 
            Q(publisher__icontains=query) |
            Q(staff__fullname__icontains=query) | 
            Q(release_year__icontains=query)
            ).distinct()

    user = request.user
    for book in book_list:
        if book.likes.filter(id=user.id).exists():
            liked_books.append(book)

    paginator = Paginator(book_list, 12) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        books = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        books = paginator.page(paginator.num_pages)

    data = {"title":"Book part of the web site!",
            "books" : books,
            "liked_books" : liked_books,

            }
    return render(request, 'books/index.html', data)

def book_detail(request, **kwargs):
    book = get_object_or_404(Book, id=kwargs.get('book_id'))
    context = {
        "title":"Book detail",
        "book" : book,
        "author" : book.get_authors,
    }
    return render(request, 'books/book_detail.html', context)

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

def addBook(request):
    
    form = BookForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        #data = instance.cleaned_data
        
        #data['fullname'] = data['firstname'] + " " + data['lastname']
        print(form.cleaned_data)
        # === add Movie
        title = form.cleaned_data.get('title', None)
        if not Book.objects.filter(title__iexact = title).exists():
                book = Book(title = title)
                book.save()
        else: 
            book = Book.objects.get(title = title)

        # add Directors
        # directors = form.cleaned_data.get('directors', None)
        # if directors is not None:
        #     print(directors)
        #     for director in directors.split(','):
        #         director_name = director.strip()
        #         if Person.objects.filter(fullname__iexact = director_name ).exists():
        #             person = Person.objects.filter(fullname__iexact = director_name)[0]
        #             role = Role.objects.filter(title__iexact = 'director' )[0]
        #             workon = WorkedOn(person = person , movie = movie, role = role )
        #             workon.save()
    context = {
        "title":"Add Person",
        "form":form
    }
    return render(request, 'movies/addperson.html', context)

