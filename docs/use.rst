How to Use Mapistration
========================

Follow Installing Instructtions First


Template Changes
================  
1) Add a div in your user registration template . Make sure it has a id='map_canvas'

2) Add {% include 'maps' %} . Make sure this include tag is below the div created above
		
	
Form Changes
=============
1) Make your Registration form inherit the LocationForm from the app

	from mapistration.forms import LocationForm
	
	class UserForm(LocationForm):
		full_name = forms.CharField(max_length=50) #example

Model Changes
=============
1) Link your registration model to mapistration Place Model
You can use OneToOneField or ForeignKey according to your requiremnts.

	from mapistration.models import Place	

	class UserRegistrationModel(models.Model):
		location = models.OneToOneField(Place)
