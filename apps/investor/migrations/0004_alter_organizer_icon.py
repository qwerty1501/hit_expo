# Generated by Django 3.2.9 on 2023-07-26 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0003_organizer_sponsors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizer',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото иконки'),
        ),
    ]
