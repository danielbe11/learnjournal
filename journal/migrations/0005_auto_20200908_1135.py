# Generated by Django 3.1.1 on 2020-09-08 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0004_resource_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='framework',
            field=models.CharField(blank=True, choices=[('Flash', 'Flash'), ('Django', 'Django'), ('SpringBoot', 'SpringBoot'), ('Angular', 'Angular')], max_length=30),
        ),
        migrations.AlterField(
            model_name='resource',
            name='language',
            field=models.CharField(choices=[('Python', 'Python'), ('Ruby', 'Ruby'), ('Java', 'Java'), ('JavaScript', 'JavaScript')], max_length=30),
        ),
    ]
