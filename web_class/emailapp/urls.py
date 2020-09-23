from django.urls import path

from .views import form_view, render_form

app_name = 'email'

urlpatterns = [
    path('render-form/', render_form, name='render_form'),
    path('email_verification', form_view, name='form_view')
]
