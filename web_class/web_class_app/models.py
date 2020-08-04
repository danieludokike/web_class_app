from django.db import models


class TutorialCourses(models.Model):
    """Provides fields for the offer for the programming courses"""
    course_name = models.CharField(max_length=12)
    course_title = models.CharField(max_length=20)
    course_description = models.TextField()
    pub_date = models.DateTimeField('Date Published')

    def __str__(self):
        """Returns the title of the course"""
        return self.course_name




