from django.db import models
from datetime import datetime, date

class Resource(models.Model):
    name_text = models.CharField(max_length=200)
    link = models.URLField()
    # attachment =
    PYTHON = 'PY'
    RUBY = 'RU'
    JAVA = 'JA'
    JAVASCRIPT = 'JS'
    LANGUAGE_CHOICES  = [
        (PYTHON, 'Python'),
        (RUBY, 'Ruby'),
        (JAVA, 'Java'),
        (JAVASCRIPT, 'JavaScript'),
    ]
    language = models.CharField(max_length=2,
        choices=LANGUAGE_CHOICES,
        blank=False)
    FLASH = 'FL'
    DJANGO = 'DJ'
    SPRINGBOOT = 'SP'
    ANGULAR = 'AN'
    FRAMEWORK_CHOICES = [
        (FLASH, 'Flash'),
        (DJANGO, 'Django'),
        (SPRINGBOOT, 'Springboot'),
        (ANGULAR, 'Angular')
    ]
    framework = models.CharField(max_length=2,
        choices=FRAMEWORK_CHOICES,
        blank=True)
    notes = models.CharField(max_length=1000, blank='True')
    # database =
    # technology =
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name_text

