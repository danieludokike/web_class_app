# Generated by Django 3.0.8 on 2020-08-05 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_class_app', '0005_usercontactform'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('course_details', models.TextField()),
            ],
        ),
    ]