from django import forms

from .models import  Movie ,Actor

import autocomplete_light

class ActorForm(forms.ModelForm):
	class Meta:
		model = Actor
		fields = ['firstname','lastname', 'gender', 'age', 'date_of_birth', 'date_of_death', 
					'place_of_birth', 'place_of_death', 'biography']
		

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
	class Meta: 
		model = Movie
		exclude = ['timestamp', 'update']
		autocomplete_fields = ('geners','directors','writers','actors')
		widgets = {
            'geners': autocomplete_light.widgets.TextWidget('MovieGenerAutocomplete'),
            'directors': autocomplete_light.widgets.TextWidget('MovieDirectorAutocomplete'),
            'writers': autocomplete_light.widgets.TextWidget('MovieWriterAutocomplete'),
            'actors': autocomplete_light.widgets.TextWidget('MovieActorAutocomplete'),
        }

