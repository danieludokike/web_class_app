from django.urls import path

from .views import (
    user_profile_page_view,
    registration_page_view,
    login_page_view,
    logout_view,
    login_required_redirection_view,
    home_page_view,
    about_web_class_page_view,
    contact_page_view,
    search_result_page_view,
    tutorial_page_view,

)

app_name = 'web_class'
urlpatterns = [
    path('', home_page_view, name='home'),
    path('web_class/about/', about_web_class_page_view, name='about'),
    path('contact/', contact_page_view, name='contact'),

    path('account/register/', registration_page_view, name='register'),
    path('account/login/', login_page_view, name='login'),
    path('account/user/logout/', logout_view, name='logout'),
    path('account/login/required/', login_required_redirection_view, name='login_required'),
    path('account/user/profile/', user_profile_page_view, name='profile'),

    path('web_class/tutorial/', search_result_page_view, name='tutorial-search'),
    path('web_class/tutorial/<str:course_name>/', tutorial_page_view, name='course_details')

]
