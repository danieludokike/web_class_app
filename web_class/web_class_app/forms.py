from django import forms


# Forms to be inherited from
class BaseForm(forms.Form):
    """The registration and the login form inherits from this"""
    username = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username*',
                'class': 'form-control',
            }
        )
    )
    password = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control',
            }
        )
    )

    abstract = True


# User Registration form
class RegistrationForm(BaseForm):
    """The User Registration form"""
    email = forms.CharField(
        max_length=255,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email*',
                'class': 'form-control',
            }
        )
    )

    password2 = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Re-.'
                               '.Enter Password',
                'class': 'form-control',
            }
        )
    )


# User Login Form
class LoginForm(BaseForm):
    """The User Login form"""
