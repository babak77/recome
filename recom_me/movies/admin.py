from django.contrib import admin

# Register your models here.
from .models import *


# class MovieAdmin(admin.ModelAdmin):
# 	list_display = ["__str__", "pub_date"]
# 	class Meta:
# 		model = Movie


admin.site.register(Movie)
admin.site.register(Writer)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Gener)

