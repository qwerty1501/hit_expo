# Generated by Django 4.2.3 on 2023-07-26 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advantage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Преимущество',
                'verbose_name_plural': 'Преимущества',
            },
        ),
        migrations.CreateModel(
            name='Conditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('signing', models.CharField(max_length=300, verbose_name='Подописание')),
            ],
            options={
                'verbose_name': 'Условия участия',
                'verbose_name_plural': 'Условия участия',
            },
        ),
        migrations.CreateModel(
            name='GeneralAdvantages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='media/invest_zone', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Общие Преимущества',
                'verbose_name_plural': 'Общие Преимущества',
            },
        ),
        migrations.CreateModel(
            name='ParticipationSteps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='media/invest_zone', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Этап участия',
                'verbose_name_plural': 'Этапы участия',
            },
        ),
        migrations.CreateModel(
            name='StandZone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtext', models.CharField(max_length=300, verbose_name='Текст об окончании бронирования')),
            ],
            options={
                'verbose_name': 'Зона Стенда',
                'verbose_name_plural': 'Зона Стенда',
            },
        ),
        migrations.CreateModel(
            name='Terms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Условия у Стенда',
                'verbose_name_plural': 'Условия у Стендов',
            },
        ),
        migrations.CreateModel(
            name='Stand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
                ('number_of_places', models.PositiveIntegerField(verbose_name='Кол-во мест')),
                ('terms', models.ManyToManyField(to='invest_zone.terms', verbose_name='Условия у Стенда')),
            ],
            options={
                'verbose_name': 'Стенд',
                'verbose_name_plural': 'Стенды',
            },
        ),
        migrations.CreateModel(
            name='InvestZone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_title', models.CharField(max_length=300, verbose_name='Заглавный текст')),
                ('header_photo', models.ImageField(upload_to='media/invest_zone', verbose_name='Заглавное фото')),
                ('number_of_members', models.PositiveIntegerField(verbose_name='Кол-во участников')),
                ('advantage', models.ManyToManyField(to='invest_zone.advantage', verbose_name='Преимущества')),
            ],
            options={
                'verbose_name': 'Начало',
                'verbose_name_plural': 'Начало',
            },
        ),
    ]
