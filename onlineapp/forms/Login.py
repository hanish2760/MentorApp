from django import forms

class loginForm(forms.Form):
    username=forms.CharField(
        max_length=25,
        widget=forms.TextInput(attrs={
        'class':'form-control','placeholder':'First Name',
        }),
        required= True,
    )
    password = forms.CharField(
        max_length=25,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 'placeholder': 'Enter Student name',
        }),
        required=True,
    )
