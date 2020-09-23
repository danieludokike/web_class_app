from django import forms


class EmailVerificationForm(forms.Form):
    """The Email verification form"""
    email = forms.EmailField()
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password'
        })
    )