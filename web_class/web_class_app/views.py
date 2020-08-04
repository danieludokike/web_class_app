from django.shortcuts import render

from django.http import HttpResponse

from . forms import (
    RegistrationForm,
    LoginForm,
)

from . models import TutorialCourses


def home_page_view(request):
    """Renders the home page on request"""

    query_set = TutorialCourses.objects.all()
    template = 'web_class/index.html'

    context = {
        'available_courses': query_set
    }
    return render(request, template, context)


def about_web_class_page_view(request):
    """Renders the about web_class page"""
    template = 'web_class/about.html'

    context = {

    }
    return render(request, template, context)




# User Registration Page
def registration_page_view(request):
    """Renders the User Registration Form"""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
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
    if request.method == 'POST':
        form = LoginForm(request.POST)
    else:
        form = LoginForm()
        template = 'web_class/account/login.html'

        context = {
            'form': form,
        }
        return render(request, template, context)


# User Profile Page
def user_profile_page_view(request):
    """Renders the User Profile Page"""
    template = 'web_class/account/profile.html'

    context = {

    }
    return render(request, template, context)


# User Profile Editing Page
def user_profile_edith_page_view(request):
    """Renders the User Profile edith Page"""
    template = 'web_class/account/edith_profile.html'

    context = {

    }
    return render(request, template, context)