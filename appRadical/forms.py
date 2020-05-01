from django import forms
from .models import Subscribe, Contact, Purchase


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ['email']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'message': forms.TextInput(attrs={'placeholder': 'Message'}),
        }
        fields = ['full_name', 'email', 'message']


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        widgets = {
            'client_name': forms.TextInput(attrs={'placeholder': 'Client Name'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email Address'}),
        }
        fields = ['client_name', 'phone_number', 'email']
