from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Movie)
admin.site.register(Writer)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Gener)