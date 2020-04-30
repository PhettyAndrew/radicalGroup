from django import forms
from .models import Subscribe, Contact


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
