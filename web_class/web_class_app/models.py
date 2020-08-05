from django.db import models


# AVAILABLE COURSES
class TutorialCourses(models.Model):
    """Provides fields for the offer for the programming courses"""
    course_name = models.CharField(max_length=12)
    course_title = models.CharField(max_length=20)
    course_description = models.TextField()
    pub_date = models.DateTimeField('Date Published')

    def __str__(self):
        """Returns the title of the course"""
        return self.course_name


# CONTACT FORM
class UserContactForm(models.Model):
    """Contact Me Form"""
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    text = models.TextField(blank=False)

    def __str__(self):
        return self.name





