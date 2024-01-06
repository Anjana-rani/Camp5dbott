

from django import forms

class MyLoginForm(forms.Form):

        username = forms.CharField()
        password = forms.CharField(widget=forms.PasswordInput)



from .models import Customer



from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


    
    


# forms.py in ottapp
from django import forms
from .models import Customer

# forms.py in ottapp
from django import forms
from .models import Customer

class CustomerRegistrationForm(forms.ModelForm):
    PAYMENT_CHOICES = [
        ('basic', 'Basic'),
        ('standard', 'Standard'),
        ('premium', 'Premium'),
    ]

    payment_method = forms.ChoiceField(
        label="Payment Method",
        choices=PAYMENT_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = Customer
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'dob', 'phone_number', 'payment_method']

    def clean_dob(self):
        dob = self.cleaned_data.get('dob')
        if dob and dob.year >= 2015:
            raise forms.ValidationError("Date of birth must be before 2015")
        return dob

       
