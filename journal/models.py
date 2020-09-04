from django.db import models

# Create your models here.
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
    FRAMEWORK_CHOICES  = [
        (FLASH, 'Flash'),
        (DJANGO, 'Django'),
        (SPRINGBOOT, 'Springboot'),
        (ANGULAR, 'Angular')
    ]
    framework = models.CharField(max_length=2,
        choices=FRAMEWORK_CHOICES,
        blank=True)
    # database =
    # technology =
    # pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.name_text

