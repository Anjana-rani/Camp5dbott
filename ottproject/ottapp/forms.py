
# ottapp/forms.py

from django import forms

class MyLoginForm(forms.Form):

        username = forms.CharField()
        password = forms.CharField(widget=forms.PasswordInput)



from .models import Customer



from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer  # Replace 'Customer' with your actual model name
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'dob', 'phone_number']

    def clean_dob(self):
        dob = self.cleaned_data.get('dob')
        if dob and dob.year >= 2015:
            raise ValidationError(_("Date of birth must be before 2015"))
        return dob