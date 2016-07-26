from django import forms
from django.contrib.auth import authenticate
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

    cur_user = None

    def get_logged_in_user(self):
        return self.cur_user

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        self.cur_user = authenticate(username=username, password=password)
        if (not self.cur_user) or (not self.cur_user.is_active):
            raise forms.ValidationError("Invalid username or password. Please try again.")

        return self.cleaned_data

class RegistrationForm(forms.Form):
    #username is email
    username = forms.EmailField(
        label = 'Email',
        max_length = 255,
        widget = forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Email',

            }
        ),
    )
    password1 = forms.CharField(
        label = 'Your Password',
        widget = forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Password',
            }
        ),
    )
    password2 = forms.CharField(
        label = 'Please Type Your Password Again',
        widget = forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Confirm Password',
            }
        ),
    )

    first_name = forms.CharField(
        label = 'First Name',
        max_length = 50,
        widget = forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': 'First Name',
            }
        ),
    )

    last_name = forms.CharField(
        label = 'Last Name',
        max_length = 50,
        widget = forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Last Name',
            }
        ),
    )

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return self.cleaned_data
