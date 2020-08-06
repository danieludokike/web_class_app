from django.contrib import admin

from . models import TutorialCourses, UserContactForm, CourseDetails


class TutorialCoursesAdmin(admin.ModelAdmin):
    """Shows a list display in the database"""
    list_display = [
        'course_name',
        'course_title',
        'pub_date',
    ]


class UserContactFormAdmin(admin.ModelAdmin):
    """Displays tabular form of the users"""
    list_display = [
        'name',
        'email',
        'subject',
    ]


# Registering Models
admin.site.register(CourseDetails)
admin.site.register(TutorialCourses, TutorialCoursesAdmin)
admin.site.register(UserContactForm, UserContactFormAdmin)
