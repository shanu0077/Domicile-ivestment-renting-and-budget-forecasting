from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import NormalUser, HotelOwner, CabDriver

class NormalUserForm(forms.Form):
    firstname = forms.CharField(label='Firstname', max_length=100, min_length=2,
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your first name'}))
    lastname = forms.CharField(label='Lastname', max_length=100, min_length=1,
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your last name'}))
    phone = forms.CharField(label='Phone number', max_length=35, min_length=10,
                             widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Mobile No.'}))
    email = forms.EmailField(label='Email', max_length=35, min_length=5,
                             widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Enter Email ID'}))
    password1 = forms.CharField(label='Password', max_length=50, min_length=5,
                                widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'New Password'}))
    password2 = forms.CharField(label='Confirm Password',
                                max_length=50, min_length=5,
                                widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Confirm Password'}))



class HotelUserForm(forms.Form):
    firstname = forms.CharField(label='Firstname', max_length=100, min_length=2,
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your first name'}))
    lastname = forms.CharField(label='Lastname', max_length=100, min_length=1,
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your last name'}))
    email = forms.EmailField(label='Email', max_length=35, min_length=5,
                             widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Enter Email ID'}))
    password1 = forms.CharField(label='Password', max_length=50, min_length=5,
                                widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'New Password'}))
    password2 = forms.CharField(label='Confirm Password',
                                max_length=50, min_length=5,
                                widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Confirm Password'}))



# class HotelOwnerForm(UserCreationForm):
#     class Meta:
#         model = HotelOwner
#         fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')

# class CabDriverForm(UserCreationForm):
#     class Meta:
#         model = CabDriver
#         fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')
