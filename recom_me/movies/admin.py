from django.contrib import admin

# Register your models here.
from .models import *


class MovieAdmin(admin.ModelAdmin):
	list_display = ('title', 'actor_names', 'director_names', 'producer_names' )
	#fields = ['title', '']
	# list_display = ('title','directors_names','actors_names')
	prepopulated_fields = {'slug': ('title', )}
	class Meta:
		model = Movie
	def actor_names(self, obj):
		staff_list = []
		try:
			actors = obj.workedon_set.filter(role__title='actor')
			for actor in actors:
				print(actor.person.fullname)
				if actor.person.fullname not in staff_list:
					staff_list.append(actor.person.fullname )
		except:
			pass
			
		return ', '.join(staff_list)

	def director_names(self, obj):
		staff_list = []
		try:
			directors = obj.workedon_set.filter(role__title='director')
			for director in directors:
				print(director.person.fullname)
				if director.person.fullname not in staff_list:
					staff_list.append(director.person.fullname )
		except:
			pass

		return ', '.join(staff_list)

	def producer_names(self, obj):
		staff_list = []
		try:
			producers = obj.workedon_set.filter(role__title='producer')
			for producer in producers:
				print("producer= ",producer.person.fullname)
				if producer.person.fullname not in staff_list:
					staff_list.append(producer.person.fullname )
		except:
			pass

		return ', '.join(staff_list)

	# def Musiccomposer_names(self, obj):
	# 	staff_list = []
	# 	try:
	# 		composers = obj.workedon_set.filter(role__title='music')
	# 		for composer in composers:
	# 			print("producer= ",composer.person.fullname)
	# 			if composer.person.fullname not in staff_list:
	# 				staff_list.append(composer.person.fullname )
	# 	except:
	# 		pass

	# 	return ', '.join(staff_list)
	
	director_names.short_description = "Directors"
	producer_names.short_description = "Producers"



# class PersonAdmin(admin.ModelAdmin):
#     list_display = ('fullname','firstname', 'lastname' , 'nationality' )

# class MovieAdmin(admin.ModelAdmin):
# 	list_display = ('title','directors_names') #, 'writers','actors' ,'screenplays', 'producers', 'editing', 'cinematography','musicComposers' )
# 	class Meta:
# 		model = Movie
admin.site.register(Movie, MovieAdmin)
admin.site.register(Person)
admin.site.register(Gener)
# admin.site.register(Occupation)
admin.site.register(Role)
admin.site.register(WorkedOn)
admin.site.register(Rating)
