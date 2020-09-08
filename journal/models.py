from django.db import models
from datetime import datetime, date


class Resource(models.Model):
    name_text = models.CharField(max_length=200)
    link = models.URLField()
    attachment = models.FileField(upload_to='journal/attachments/', null=True, blank=True)
    PYTHON = 'Python'
    RUBY = 'Ruby'
    JAVA = 'Java'
    JAVASCRIPT = 'JavaScript'
    LANGUAGE_CHOICES = [
        (PYTHON, 'Python'),
        (RUBY, 'Ruby'),
        (JAVA, 'Java'),
        (JAVASCRIPT, 'JavaScript'),
    ]
    language = models.CharField(max_length=30,
                                choices=LANGUAGE_CHOICES,
                                blank=False)
    FLASH = 'Flash'
    DJANGO = 'Django'
    SPRINGBOOT = 'SpringBoot'
    ANGULAR = 'Angular'
    FRAMEWORK_CHOICES = [
        (FLASH, 'Flash'),
        (DJANGO, 'Django'),
        (SPRINGBOOT, 'SpringBoot'),
        (ANGULAR, 'Angular')
    ]
    framework = models.CharField(max_length=30,
                                 choices=FRAMEWORK_CHOICES,
                                 blank=True)
    notes = models.CharField(max_length=1000, blank='True')
    # database =
    # technology =
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name_text

