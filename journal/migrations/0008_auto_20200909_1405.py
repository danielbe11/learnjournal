# Generated by Django 3.1.1 on 2020-09-09 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0007_auto_20200908_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='language',
            field=models.CharField(blank=True, choices=[('Python', 'Python'), ('Ruby', 'Ruby'), ('Java', 'Java'), ('JavaScript', 'JavaScript')], max_length=30),
        ),
    ]