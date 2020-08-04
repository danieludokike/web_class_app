from django.urls import path

from . views import (
    user_profile_edith_page_view,
    user_profile_page_view,
    registration_page_view,
    login_page_view,
    home_page_view,
    about_web_class_page_view,


)


app_name = 'web_class'
urlpatterns = [
    path('', home_page_view, name='home'),
    path('web_class/about/', about_web_class_page_view, name='about'),
    path('account/register/', registration_page_view, name='register'),
    path('account/login/', login_page_view, name='login'),
    path('account/user/profile/', user_profile_page_view, name='profile'),
    path('account/user/profile/edith/', user_profile_edith_page_view, name='edith'),

]
