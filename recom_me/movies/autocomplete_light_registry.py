import autocomplete_light.shortcuts as al
from .models import Movie, Gener, Director, Writer, Actor

# This will generate a PersonAutocomplete class.
al.register(Movie,
    # Just like in ModelAdmin.search_fields.
    name = "MovieGenerAutocomplete",
    search_fields=['name'],
    choices = Gener.objects.all(),
    attrs={
        # This will set the input placeholder attribute:
        'placeholder': 'Action, drama, ...',
        # This will set the yourlabs.Autocomplete.minimumCharacters
        # options, the naming conversion is handled by jQuery.
        'data-autocomplete-minimum-characters': 1,
    },
    # This will set the data-widget-maximum-values attribute on the
    # widget container element, and will be set to
    # yourlabs.Widget.maximumValues (jQuery handles the naming
    # conversion).
    widget_attrs={
        'data-widget-maximum-values': 4,
        # Enable modern-style widget !
        'class': 'modern-style',
    },
)

al.register(Movie,
    name = "MovieDirectorAutocomplete",
    search_fields=['firstname', 'lastname'],
    choices = Director.objects.all(),
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
    name = "MovieWriterAutocomplete",
    search_fields=['firstname', 'lastname'],
    choices = Writer.objects.all(),
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
    name = "MovieActorAutocomplete",
    search_fields=['firstname', 'lastname'],
    choices = Actor.objects.all(),
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