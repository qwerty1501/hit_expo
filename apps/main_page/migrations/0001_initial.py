# Generated by Django 4.2.3 on 2023-07-21 08:08

import apps.main_page.services
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ellipse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=300, null=True, verbose_name='Компаний')),
                ('countries', models.CharField(blank=True, max_length=300, null=True, verbose_name='Стран')),
                ('meetings', models.CharField(blank=True, max_length=300, null=True, verbose_name='B2B встречи')),
                ('exhibitors', models.CharField(blank=True, max_length=300, null=True, verbose_name='Экспонентов')),
            ],
            options={
                'verbose_name': 'Эллипс',
                'verbose_name_plural': 'Эллипс',
                'db_table': 'ellipse',
            },
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300, null=True, verbose_name='Заголовок форма')),
                ('description', models.TextField(verbose_name='Описание форма')),
            ],
            options={
                'verbose_name': 'О форуме',
                'verbose_name_plural': 'О форуме',
                'db_table': 'forum',
            },
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='')),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.main_page.services.get_upload_path, verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Участник',
                'verbose_name_plural': 'Участники',
                'db_table': 'members',
            },
        ),
        migrations.CreateModel(
            name='Organizers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Название организации')),
                ('loga', models.ImageField(blank=True, null=True, upload_to=apps.main_page.services.get_upload_path, validators=[apps.main_page.services.validate_file_extension], verbose_name='Фотография нашего организаторa *(157x127)')),
            ],
            options={
                'verbose_name': 'Организатор',
                'verbose_name_plural': 'Организаторы',
                'db_table': 'organizers',
            },
        ),
        migrations.CreateModel(
            name='PageOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.main_page.services.get_upload_path, verbose_name='Фотография')),
                ('year', models.CharField(blank=True, max_length=300, null=True, verbose_name='Год')),
                ('title', models.CharField(blank=True, max_length=300, null=True, verbose_name='Заголовок Экспо')),
                ('description', models.TextField(verbose_name='Описание Экспо')),
            ],
            options={
                'verbose_name': 'Начало',
                'verbose_name_plural': 'Начало',
                'db_table': 'page_one',
            },
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Название партнёра')),
                ('loga', models.ImageField(blank=True, null=True, upload_to=apps.main_page.services.get_upload_path, validators=[apps.main_page.services.validate_file_extension], verbose_name='Логотип нашего партнёра *(157x127)')),
            ],
            options={
                'verbose_name': 'Партнёр',
                'verbose_name_plural': 'Партёры',
                'db_table': 'partners',
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('location', models.CharField(blank=True, max_length=256, null=True, verbose_name='Ссылка для локации')),
            ],
            options={
                'verbose_name': 'Локации',
                'verbose_name_plural': 'Локации',
                'db_table': 'location',
            },
        ),
        migrations.CreateModel(
            name='PlaceOffice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=300, verbose_name='Номер телефона')),
                ('mail', models.URLField(blank=True, null=True, verbose_name='Почта')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('location', models.CharField(blank=True, max_length=256, null=True, verbose_name='Ссылка для локации')),
            ],
            options={
                'verbose_name': 'Локация офиса',
                'verbose_name_plural': 'Локация офиса',
                'db_table': 'location_office',
            },
        ),
        migrations.CreateModel(
            name='Sectors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.main_page.services.get_upload_path, verbose_name='Фотография')),
                ('icon', models.ImageField(blank=True, null=True, upload_to=apps.main_page.services.get_upload_path, validators=[apps.main_page.services.validate_file_extension], verbose_name='Фотография')),
                ('title', models.CharField(blank=True, max_length=128, null=True, verbose_name='Заголовок сектора')),
                ('description', models.TextField(verbose_name='Описание сектора')),
            ],
            options={
                'verbose_name': 'Секторы',
                'verbose_name_plural': 'Секторы',
                'db_table': 'sectors',
            },
        ),
        migrations.CreateModel(
            name='Socials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whatsapp', models.URLField(blank=True, null=True, verbose_name='Whatsapp')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('telegram', models.URLField(blank=True, null=True, verbose_name='Telegram')),
                ('snapchat', models.URLField(blank=True, null=True, verbose_name='Snapchat')),
                ('tiktok', models.URLField(blank=True, null=True, verbose_name='Tiktok')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter')),
                ('youtube', models.URLField(blank=True, null=True, verbose_name='Youtube')),
                ('wechat', models.URLField(blank=True, null=True, verbose_name='Wechat')),
            ],
            options={
                'verbose_name': 'Социальный сеть',
                'verbose_name_plural': 'Социальные сети',
                'db_table': 'socials',
            },
        ),
        migrations.CreateModel(
            name='Speakers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.main_page.services.get_upload_path, verbose_name='Фотография')),
                ('name', models.CharField(max_length=300, verbose_name='Полное имя')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Спикер',
                'verbose_name_plural': 'Спикеры',
                'db_table': 'speakers',
            },
        ),
        migrations.CreateModel(
            name='Sponsors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Название спонсара')),
                ('loga', models.ImageField(blank=True, null=True, upload_to=apps.main_page.services.get_upload_path, validators=[apps.main_page.services.validate_file_extension], verbose_name='Фотография нашего спонсара *(157x127)')),
            ],
            options={
                'verbose_name': 'Спонсор',
                'verbose_name_plural': 'Спонсоры',
                'db_table': 'sponsors',
            },
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300, null=True, verbose_name='Заголовок цели')),
                ('description', models.TextField(verbose_name='Описание цели')),
            ],
            options={
                'verbose_name': 'Цель',
                'verbose_name_plural': 'Цели',
                'db_table': 'target',
            },
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=300, verbose_name='Номер задач')),
                ('description', models.TextField(verbose_name='Описание задач')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
                'db_table': 'tasks',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=256, null=True, verbose_name='Заголовок')),
                ('urel_video', models.URLField(max_length=128, verbose_name='Укажите ссылку на видео')),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
                'db_table': 'video',
            },
        ),
    ]
