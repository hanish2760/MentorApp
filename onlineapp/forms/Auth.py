from django import forms

class signupform(forms.Form):
    first_name=forms.CharField(
        max_length=25,
        widget=forms.TextInput(attrs={
        'class':'form-control','placeholder':'First Name',
        }),
        required= True,
    )
    last_name = forms.CharField(
        max_length=25,
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Last Name',
        }),
        required=True,
    )
    username = forms.CharField(
        max_length=25,
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'user name',
        }),
        required=True,
    )
    password = forms.CharField(
        max_length=25,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 'placeholder': 'Enter Student name',
        }),
        required=True,
    )