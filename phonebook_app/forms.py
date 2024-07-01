from django import forms
from .models import Contact, PhoneNumber, EmailAddress


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name',
                  'company', 'job_title', 'description']


class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        fields = ['phone_type', 'number']


class EmailAddressForm(forms.ModelForm):
    class Meta:
        model = EmailAddress
        fields = ['email']
