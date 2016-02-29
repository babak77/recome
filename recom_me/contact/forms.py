from django import forms


class ContactForm(forms.Form):
	full_name = forms.CharField(required=False, label="Your name:")
	email = forms.EmailField(required=True, label="Your E-mail:")
	message = forms.CharField(
        required=True,
        widget=forms.Textarea,
        label="Message:"
    )

