from django.shortcuts import render

# Create your views here.
def index(request):
    data = {"title":"Movie part of the web site!"}
    return render(request, 'movies/index.html', data)
