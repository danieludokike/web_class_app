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
                'placeholder': 'Password*',
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
                'placeholder': 'Password (again)*',
                'class': 'form-control',
            }
        )
    )


# User Login Form
class LoginForm(BaseForm):
    """The User Login form"""


# CONTACT FORM
class ContactMeForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Name*',
                'class': 'form-control',
            }
        )
    )

    email = forms.CharField(
        max_length=200,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Your Email*',
                'class': 'form-control',
            }
        )
    )

    subject = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Subject*',
                'class': 'form-control',
            }
        )
    )

    text = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Message',
                'class': 'text-field',
                'cols': 30,
                'rows': 7,
            }
        )
    )


