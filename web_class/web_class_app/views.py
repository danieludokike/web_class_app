from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import (
    render,
    redirect, get_object_or_404,
)

from django.contrib import messages
from django.contrib.auth.models import User

from .forms import (
    RegistrationForm,
    LoginForm,
    ContactMeForm,
)

from .models import TutorialCourses, UserContactForm, CourseDetails

import re  # Regular expression module


# Home page view functions
def home_page_view(request):
    """Renders the home page on request"""

    # Checking if User is logged in
    if request.user.is_authenticated:
        return redirect('web_class:profile')

    else:
        query_set = TutorialCourses.objects.all()[:4]
        template = 'web_class/index.html'

        context = {
            'available_courses': query_set
        }
        return render(request, template, context)


def about_web_class_page_view(request):
    """Renders the about web_class page"""

    # Checking if User is logged in
    if request.user.is_authenticated:
        return redirect('web_class:profile')

    else:
        template = 'web_class/about.html'

        context = {

        }
        return render(request, template, context)


# CONTACT PAGE
def contact_page_view(request):
    """Renders the contact page view on request"""
    if request.method == 'POST':
        name = request.POST['name'].title()
        email = request.POST['email']
        subject = request.POST['subject'].title()
        text = request.POST['text']

        if name == '' or text == '' or email == '' or subject == '':

            messages.info(request, 'Please fill out all fields')
            return redirect('web_class:contact')
        else:
            user_passed_details = UserContactForm(
                name=name,
                email=email,
                subject=subject,
                text=text,
            )
            user_passed_details.save()

            messages.info(request, "Hello " + name + ", Thanks for leaving me a message"
                                                     " We will be in touch with your provided email.")
            return redirect('web_class:login_required')

    else:
        template = 'web_class/contact.html'

        context = {
            # Sending date to page and requested objects
            'form': ContactMeForm
        }
        return render(request, template, context)


# User Registration Page
def registration_page_view(request):
    """Renders the User Registration Form"""

    # Checking if User is logged in
    if request.user.is_authenticated:
        return redirect('web_class:profile')

    else:

        form = RegistrationForm()
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['password2']

            # Field validation
            if username.isupper():
                messages.info(request, "Signup Error: Username must be in all lowercase.")
                return redirect("web_class:register")

            if email.isupper():
                messages.info(request, "Signup Error: Email must be in all lowercase.")
                return redirect("web_class:register")

            if username == '' or email == '' or password == '' or password2 == '':
                messages.info(request, "Signup Error: Please fill out all fields.")
                return redirect("web_class:register")

            # Checking if the Username already exists in the database
            if User.objects.filter(username=username).exists():
                messages.info(request, "Signup Error: Username already taken.")
                return redirect("web_class:register")

            # Username validation
            if not re.search(r'^\w+$', username):
                messages.info(request, "Signup Error: Invalid Username. Username must be alphanumeric and may contain "
                                       "and underscore")
                return redirect("web_class:register")

            # Email validation
            if User.objects.filter(email=email).exists():
                messages.info(request, "Signup Error: Email already taken.")
                return redirect("web_class:register")

            # Password validation
            if password != password2:
                messages.info(request, "Signup Error: Passwords do not match!!.")
                return redirect("web_class:register")

            if len(password) < 8:
                messages.info(request, "Signup Error: Password length must be minimum of eight (8) characters")
                return redirect("web_class:register")

            user = User.objects.create_user(
                username=username.upper(),
                email=email,
                password=password
            )
            user.save()

            alert_msg = "Hello " + username.title() + "!! Your account creation was successful. Proceed to login"
            messages.add_message(request, messages.INFO, alert_msg)
            return redirect('web_class:login_required')

        else:
            form = RegistrationForm()
            template = 'web_class/account/register.html'

            context = {
                'form': form,
            }
            return render(request, template, context)


# User Login Page
def login_page_view(request):
    """Renders the User Login form and Process's it"""

    # Checking if User is logged in
    if request.user.is_authenticated:
        return redirect('web_class:profile')

    else:
        form = LoginForm()
        if request.method == 'POST':
            form = LoginForm(request.POST)
            username = request.POST['username']
            password = request.POST['password']

            # Validating Username
            if username.isupper():
                messages.info(request, "Authentication Error: Invalid Username or Password.Note: fields may be "
                                       "case sensitive")
                return redirect("web_class:login")

            username = username.upper()
            user = authenticate(
                username=username,
                password=password,
            )

            # Validation User's credentials
            if user is not None:
                login(request, user)
                return redirect('web_class:profile')
            else:
                messages.info(request, "Authentication Error: Invalid Username or Password. Note: both fields may be "
                                       "case sensitive")
                return redirect("web_class:login")

        else:
            template = 'web_class/account/login.html'

            context = {
                'form': form,
            }
            return render(request, template, context)


def logout_view(request):
    """Logs the User out"""
    logout(request)
    messages.add_message(request, messages.INFO, 'Thanks for taking courses in our platform!!')
    return redirect('web_class:login_required')


# User Profile Page
@login_required(login_url='web_class:login_required')
def user_profile_page_view(request):
    """Renders the User Profile Page"""
    query_set = TutorialCourses.objects.all()[:4]
    template = 'web_class/account/profile.html'

    context = {
        'available_courses': query_set
    }
    return render(request, template, context)


# User Profile Editing Page
def login_required_redirection_view(request):
    """Renders the User Profile edith Page"""

    # Checking if the User is logged in
    if request.user.is_authenticated:
        return redirect('web_class:profile')
    else:
        template = 'web_class/account/login_redirect.html'

        context = {

        }

        return render(request, template, context)


# Handle search for tutorials
def search_result_page_view(request):
    """Renders and shows the search result"""
    if request.method == 'POST':
        course_name = request.POST['search']

        # Checking if field is empty
        if course_name == '':
            messages.info(request, 'Please enter something in the search field')
            return redirect('web_class:profile')

        course_name = course_name.upper()
        get_course = TutorialCourses.objects.filter(course_name=course_name)
        template = 'web_class/tutorial.html'
        context = {
            'course': get_course,
            'course_name': course_name.title(),
        }
        return render(request, template, context)

    else:
        template = 'web_class/tutorial.html'

        context = {

        }
        return render(request, template, context)


# Displays the tutorial text to the user
def tutorial_page_view(request, course_name):
    """Renders the tutorial page for the user"""

    course = get_object_or_404(CourseDetails, title=course_name)
    template = 'web_class/account/tutorial_display.html'

    context = {
        'course': course,
    }
    return render(request, template, context)



