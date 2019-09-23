from django.db import models

# Create your models here.

#Model that represents the information that needs to be sent to me. Similar
#to an object, this will be used to map to the database (ORM).
class Contact(models.Model):

	RELATIONS=(
		('None', 'none'),
		('Family', 'family'),
		('Friend', 'friday'),
		('Professor', 'professor'),
		('Student', 'student'),
		('Worker', 'work'),
	)
	
	name = models.CharField(max_length=45)
	email = models.CharField(max_length=55)
	message = models.TextField()
	relation = models.CharField(max_length=9, choices=RELATIONS, default='None')
