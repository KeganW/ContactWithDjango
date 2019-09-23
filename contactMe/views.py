from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from .models import Contact

# Create your views here.

#simply loads the home screen as contact.html.j2
def home(request):
	return render(request, 'contacts.html.j2')

#method executed when submit button is clicked
def inform(request):
	valid_email = False

	#retrieve information, form is not yet submitted
	if request.method == 'POST':
		
		name = request.POST['name']
		email = request.POST['email']
		message = request.POST['message']
		relation = request.POST['occupation']

	valid_email = val_email(email)

	print(len(name))
	print(len(message))

	#validity checks for user input
	if (len(name) == 0 or len(message) == 1):
		error = "One or more fields has empty input. The form was not submitted. Please try again."
		return render(request, 'contacts.html.j2', {'error': error})	

	
	elif (not valid_email):
		error = "Invalid email. The form was not submitted. Please try again."
		return render(request, 'contacts.html.j2', {'error': error})

	#submit form and input into database		
	else:	
		#success message to be displayed
		success = name + ", your form has been submitted. I will try my best to get back to you in a timely manner."
		#insert into database
		contact_info = Contact(name = name, email = email, message = message,
							relation = relation)
		contact_info.save()	

		return render(request, 'contacts.html.j2', {'success': success})

#helper method that verifies emails
def val_email(email):
	validator = EmailValidator()
	try:
		validator(email)
	except ValidationError:
		return False

	return True
