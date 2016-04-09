from django import forms

from .models import  Person, Gener, Book

import autocomplete_light

class PersonForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = [ ] 
		exclude = ['timestamp', 'update', 'slug']
		widgets = {
			'date_of_birth': forms.DateInput(format=('%Y-%m-%d'), 
                                             attrs={'class':'myDateClass', 
                                            'placeholder':'ex: 1991-10-04'}),
            'date_of_death': forms.DateInput(format=('%Y-%m-%d'), 
                                             attrs={'class':'myDateClass', 
                                            'placeholder':'ex: 1991-10-04'}),
            #'occupations': autocomplete_light.widgets.MultipleChoiceWidget('PersonOccupationAutocomplete'),
            
        }

class BookForm(forms.ModelForm):
	# directors = forms.CharField(max_length=200, required=False, widget=autocomplete_light.widgets.TextWidget('MovieStaffAutocomplete'))
	# writers = forms.CharField(max_length=200, required=False, widget=autocomplete_light.widgets.TextWidget('MovieStaffAutocomplete'))
	# actors = forms.CharField(max_length=200, required=False, widget=autocomplete_light.widgets.TextWidget('MovieStaffAutocomplete'))
	# producers = forms.CharField(max_length=200, required=False, widget=autocomplete_light.widgets.TextWidget('MovieStaffAutocomplete'))
	# musicComposers = forms.CharField(max_length=200, required=False, widget=autocomplete_light.widgets.TextWidget('MovieStaffAutocomplete'))
	# screenplays = forms.CharField(max_length=200, required=False, widget=autocomplete_light.widgets.TextWidget('MovieStaffAutocomplete'))
	# editing = forms.CharField(max_length=200, required=False, widget=autocomplete_light.widgets.TextWidget('MovieStaffAutocomplete'))
	# cinematography = forms.CharField(max_length=200, required=False, widget=autocomplete_light.widgets.TextWidget('MovieStaffAutocomplete'))
	class Meta: 
		model = Book
		exclude = ['timestamp', 'update', 'staff', 'likes', 'slug']
		#autocomplete_fields = ('title','geners','directors','writers','actors', 'producers', 'screenplay', 'editing', 'cinematography','musicComposers')
		autocomplete_fields = ('directors',)
		
		widgets = {
			'pub_date': forms.DateInput(format=('%Y-%m-%d'), 
                                             attrs={'class':'myDateClass', 
                                            'placeholder':'ex: 1991-10-04'}),
			'gener': forms.CheckboxSelectMultiple(),

		}
