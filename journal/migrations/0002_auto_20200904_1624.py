# Generated by Django 3.1.1 on 2020-09-04 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='framework',
            field=models.CharField(blank=True, choices=[('FL', 'Flash'), ('DJ', 'Django'), ('SP', 'Springboot'), ('AN', 'Angular')], max_length=2),
        ),
        migrations.AlterField(
            model_name='resource',
            name='language',
            field=models.CharField(choices=[('PY', 'Python'), ('RU', 'Ruby'), ('JA', 'Java'), ('JS', 'JavaScript')], max_length=2),
        ),
    ]