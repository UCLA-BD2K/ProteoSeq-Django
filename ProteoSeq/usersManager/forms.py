from django import forms
from django.contrib.auth import authenticate,login
class LoginForm(forms.Form):
    # this case, username is the same as email
    username = forms.CharField(
        label = 'Email',
        max_length = 255,
        widget = forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Email',
            }
        ),
    )
    password = forms.CharField(
        label = 'Password',
        widget = forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Password',
            }
        ),
    )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if (not user) or (not user.is_active):
            raise forms.ValidationError("Invalid username or password. Please try again.")
        else:
            login(request,user)
        return self.cleaned_data
