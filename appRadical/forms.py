from django import forms
from .models import Subscribe


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ['email']
