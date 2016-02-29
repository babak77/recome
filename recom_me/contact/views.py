from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import ContactForm

# Create your views here.
def contact(request):
	title = "Contact Us"
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form_full_name = form.cleaned_data.get('full_name')
		form_email = form.cleaned_data.get('email')
		form_message = form.cleaned_data.get('message')
		subject = 'Site Contact Form'
		from_email = settings.EMAIL_HOST_USER
		to_email_list = [from_email]
		contact_message = "{} : {} via {}".format(form_full_name, form_message, form_email)

		send_mail(subject, contact_message, from_email, to_email_list , fail_silently=False)

	context = {
    	"form":form,
    	"title": title,
    }

	return render(request, 'contact/contact.html', context)
