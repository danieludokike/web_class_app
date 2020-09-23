from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect

from .forms import EmailVerificationForm


def form_view(request):
    """Renders the email verification form"""
    form = EmailVerificationForm()
    email = request.POST['email']
    password = request.POST['password']

    subject = 'Student Registration'
    message = 'YOur Registration was successful..' + email + '..' + password
    from_email = 'webemailsender523@gmail.com'
    recipient = [email]
    send_mail(subject, message, from_email, recipient)
    print(email)

    return redirect('/')


def render_form(request):
    form = EmailVerificationForm()
    template = 'web_class/emailapp/email_verification.html'

    context = {
        'form': form,
    }
    return render(request, template, context)
