# Generated by Django 3.1.1 on 2020-09-08 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0006_resource_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='journal/attachments/'),
        ),
    ]
