from django.contrib import admin

from .models import *
# Register your models here.

class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author' )
	prepopulated_fields = {'slug': ('title', )}
	class Meta:
		model = Book

	def author(self, obj):
		staff_list = []
		try:
			authors = obj.workedon_set.filter(role__title='author')
			for author in authors:
				print(author.person.fullname)
				if author.person.fullname not in staff_list:
					staff_list.append(author.person.fullname )
		except:
			pass
			
		return ', '.join(staff_list)

admin.site.register(Book, BookAdmin)
admin.site.register(Person)
admin.site.register(Gener)
admin.site.register(Role)
admin.site.register(WorkedOn)
admin.site.register(Rating)