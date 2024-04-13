from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class BookingForm(forms.Form):
    num_tickets = forms.IntegerField(min_value=1, label='Number of Tickets')

    def clean_num_tickets(self):
        num_tickets = self.cleaned_data['num_tickets']
        if num_tickets <= 0:
            raise forms.ValidationError("Number of tickets must be greater than zero.")
        return num_tickets
