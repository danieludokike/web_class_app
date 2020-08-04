from django.contrib import admin

from . models import TutorialCourses


class TutorialCoursesAdmin(admin.ModelAdmin):
    """Shows a list display in the database"""
    list_display = [
        'course_name',
        'course_title',
        'pub_date',
    ]


# Registering Models
admin.site.register(TutorialCourses, TutorialCoursesAdmin)

