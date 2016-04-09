import autocomplete_light.shortcuts as al
from .models import Movie, Person
#from .models import Movie, Gener, Person, Occupation

# This will generate a PersonAutocomplete class.
# al.register(Movie,
#     # Just like in ModelAdmin.search_fields.
#     name = "MovieGenerAutocomplete",
#     search_fields=['name'],
#     choices = Gener.objects.all(),
#     attrs={
#         # This will set the input placeholder attribute:
#         'placeholder': 'Action, drama, ...',
#         # This will set the yourlabs.Autocomplete.minimumCharacters
#         # options, the naming conversion is handled by jQuery.
#         'data-autocomplete-minimum-characters': 1,
#     },
#     # This will set the data-widget-maximum-values attribute on the
#     # widget container element, and will be set to
#     # yourlabs.Widget.maximumValues (jQuery handles the naming
#     # conversion).
#     widget_attrs={
#         'data-widget-maximum-values': 4,
#         # Enable modern-style widget !
#         'class': 'modern-style',
#     },
# )

# al.register(Movie,
#     name = "MovieAutocomplete",
#     search_fields=['firstname', 'lastname'],
#     choices = Person.objects.all(),
#     attrs={
#         # This will set the input placeholder attribute:
#         'placeholder': '',
#         # This will set the yourlabs.Autocomplete.minimumCharacters
#         # options, the naming conversion is handled by jQuery
#         'data-autocomplete-minimum-characters': 1,
#     },
#     widget_attrs={
#         'data-widget-maximum-values': 4,
#         'class': 'modern-style',
#     },
# )
# al.register(Movie,
#     name = "PersonOccupationAutocomplete",
#     search_fields=['title'],
#     choices = Occupation.objects.all(),
#     attrs={
#         # This will set the input placeholder attribute:
#         'placeholder': '',
#         # This will set the yourlabs.Autocomplete.minimumCharacters
#         # options, the naming conversion is handled by jQuery
#         'data-autocomplete-minimum-characters': 1,
#     },
#     widget_attrs={
#         'data-widget-maximum-values': 4,
#         'class': 'modern-style',
#     },
# )
al.register(Movie,
    name = "MovieTitleAutocomplete",
    search_fields=['title'],
    choices = Movie.objects.all(),
    attrs={
        # This will set the input placeholder attribute:
        'placeholder': '',
        # This will set the yourlabs.Autocomplete.minimumCharacters
        # options, the naming conversion is handled by jQuery
        'data-autocomplete-minimum-characters': 1,
    },
    widget_attrs={
        'data-widget-maximum-values': 4,
        'class': 'modern-style',
    },
)

al.register(Movie,
    name = "MovieStaffAutocomplete",
    search_fields=['firstname', 'lastname'],
    choices = Person.objects.all(),
    attrs={
        # This will set the input placeholder attribute:
        'placeholder': 'Enter a name',
        # This will set the yourlabs.Autocomplete.minimumCharacters
        # options, the naming conversion is handled by jQuery
        'data-autocomplete-minimum-characters': 1,
    },
    widget_attrs={
        'data-widget-maximum-values': 4,
        'class': 'modern-style',
    },
)