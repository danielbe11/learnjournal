from django.db import models
from datetime import datetime, date


class Resource(models.Model):
    name_text = models.CharField('Resource name*', max_length=200)
    link = models.URLField('Link*')
    attachment = models.FileField('Attachment', upload_to='journal/attachments/', null=True, blank=True)
    LANGUAGE_CHOICES = [
        ('Python', 'Python'),
        ('Ruby', 'Ruby'),
        ('Java', 'Java'),
        ('JavaScript', 'JavaScript'),
    ]
    language = models.CharField('Language', max_length=30,
                                choices=LANGUAGE_CHOICES,
                                blank=True)
    FRAMEWORK_CHOICES = [
        ('Flash', 'Flash'),
        ('Django', 'Django'),
        ('SpringBoot', 'SpringBoot'),
        ('Angular', 'Angular')
    ]
    framework = models.CharField('Framework', max_length=30,
                                 choices=FRAMEWORK_CHOICES,
                                 blank=True)
    notes = models.CharField('Notes', max_length=1000, blank='True')
    post_date = models.DateField('Post date', auto_now_add=True)

    def __str__(self):
        return self.name_text

    def delete(self, *args, **kwargs):
        self.attachment.delete()
        super().delete(*args, **kwargs)
