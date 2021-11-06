from django import forms
from core.models import Contact


class ContactForm(forms.ModelForm):

	class Meta:
		model=Contact
		fields=('email','description',)
		widgets={
				
				'description':forms.Textarea(attrs={'rows':3,'cols':10,'class':'form-control mt-3','placeholder':'Description'}),


		}
