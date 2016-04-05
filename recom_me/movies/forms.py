from django import forms

from .models import  Movie ,Person, Gener , Rating

import autocomplete_light

class RatingForm(forms.ModelForm):
	class Meta:
		model = Rating
		exclude = ['timestamp', 'update', 'movie', 'user']
		widgets = {
			'rating' : forms.TextInput(attrs={'class':'rating', 'type': "number submit",
											 'data-icon-lib':"fa", 'data-active-icon' :"fa-star",
											 'data-inactive-icon':"fa-star-o"
											})
		}

class PersonForm(forms.ModelForm):
	class Meta:
		model = Person
		exclude = ['timestamp', 'update']
		# fields = ['firstname','lastname', 'gender', 'occupations','age', 'date_of_birth', 'date_of_death', 
		# 			'place_of_birth', 'place_of_death', 'biography']
		widgets = {
			'date_of_birth': forms.DateInput(format=('%Y-%m-%d'), 
                                             attrs={'class':'myDateClass', 
                                            'placeholder':'ex: 1991-10-04'}),
            'date_of_death': forms.DateInput(format=('%Y-%m-%d'), 
                                             attrs={'class':'myDateClass', 
                                            'placeholder':'ex: 1991-10-04'}),
            #'occupations': autocomplete_light.widgets.MultipleChoiceWidget('PersonOccupationAutocomplete'),
            
        }
		

# class MovieForm(forms.ModelForm):
# 	class Meta: 
# 		model = Movie
# 		exclude = ['timestamp', 'update']
# 		widgets = {
			
# 			'geners': forms.CheckboxSelectMultiple(),	
# 			#'actors': 
# 		}
	
	# OPTIONS = (
	# 		("a", "A"),
	# 		("b", "B"),
	# 		)
	# name = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTIONS)

class MovieForm(forms.ModelForm):
	directors = forms.CharField(max_length=200, required=False, widget=autocomplete_light.widgets.TextWidget('MovieStaffAutocomplete'))
	writers = forms.CharField(max_length=200, required=False, widget=autocomplete_light.widgets.TextWidget('MovieStaffAutocomplete'))
	actors = forms.CharField(max_length=200, required=False, widget=autocomplete_light.widgets.TextWidget('MovieStaffAutocomplete'))
	producers = forms.CharField(max_length=200, required=False, widget=autocomplete_light.widgets.TextWidget('MovieStaffAutocomplete'))
	musicComposers = forms.CharField(max_length=200, required=False, widget=autocomplete_light.widgets.TextWidget('MovieStaffAutocomplete'))
	screenplays = forms.CharField(max_length=200, required=False, widget=autocomplete_light.widgets.TextWidget('MovieStaffAutocomplete'))
	editing = forms.CharField(max_length=200, required=False, widget=autocomplete_light.widgets.TextWidget('MovieStaffAutocomplete'))
	cinematography = forms.CharField(max_length=200, required=False, widget=autocomplete_light.widgets.TextWidget('MovieStaffAutocomplete'))
	class Meta: 
		model = Movie
		exclude = ['timestamp', 'update', 'staff']
		#autocomplete_fields = ('title','geners','directors','writers','actors', 'producers', 'screenplay', 'editing', 'cinematography','musicComposers')
		autocomplete_fields = ('directors',)
		
		widgets = {
			'pub_date': forms.DateInput(format=('%Y-%m-%d'), 
                                             attrs={'class':'myDateClass', 
                                            'placeholder':'ex: 1991-10-04'}),
			'gener': forms.CheckboxSelectMultiple(),
			#'staff': autocomplete_light.widgets.TextWidget('MovieStaffAutocomplete'),
			# 'title': autocomplete_light.widgets.TextWidget('MovieTitleAutocomplete'),
   #          'geners': autocomplete_light.widgets.TextWidget('MovieGenerAutocomplete'),
   #          'directors': autocomplete_light.widgets.TextWidget('MovieAutocomplete'),
   #          'writers': autocomplete_light.widgets.TextWidget('MovieAutocomplete'),
   #          'actors': autocomplete_light.widgets.TextWidget('MovieAutocomplete'),
   #          'producers': autocomplete_light.widgets.TextWidget('MovieAutocomplete'),
   #          'screenplays': autocomplete_light.widgets.TextWidget('MovieAutocomplete'),
   #          'editing': autocomplete_light.widgets.TextWidget('MovieAutocomplete'),
   #          'cinematography': autocomplete_light.widgets.TextWidget('MovieAutocomplete'),
   #          'musicComposers': autocomplete_light.widgets.TextWidget('MovieAutocomplete'),

        }

