# Generated by Django 3.2.9 on 2023-07-29 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Additionally',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Дополнительная информация Стенда',
                'verbose_name_plural': 'Дополнительная информация Стенда',
            },
        ),
        migrations.CreateModel(
            name='AdditionalText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Заглавный текст')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Дополнительная информация',
                'verbose_name_plural': 'Дополнительные информации',
            },
        ),
        migrations.CreateModel(
            name='Conditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Заглавный текст')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Условия участия',
                'verbose_name_plural': 'Условия участия',
            },
        ),
        migrations.CreateModel(
            name='Decor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Информация оформление Стенда',
                'verbose_name_plural': 'Информация оформление Стенда',
            },
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='media/trade_zone', verbose_name='Логотип')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Участник',
                'verbose_name_plural': 'Участники',
            },
        ),
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Возможность',
                'verbose_name_plural': 'Возможности',
            },
        ),
        migrations.CreateModel(
            name='PurchaseStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Заглавный текст')),
                ('image', models.ImageField(upload_to='media/trade_zone', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Этап покупки',
                'verbose_name_plural': 'Этапы покупки',
            },
        ),
        migrations.CreateModel(
            name='StandPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/trade_zone')),
            ],
            options={
                'verbose_name': 'Фото Стенда',
                'verbose_name_plural': 'Фото Стендов',
            },
        ),
        migrations.CreateModel(
            name='TradeZone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_title', models.CharField(max_length=300, verbose_name='Заглавный текст')),
                ('header_photo', models.ImageField(upload_to='media/trade_zone', verbose_name='Заглавное фото')),
                ('number_of_members', models.PositiveIntegerField(verbose_name='Кол-во участников')),
                ('members', models.ManyToManyField(to='trade_zone.Members', verbose_name='Участники')),
                ('opportunity', models.ManyToManyField(to='trade_zone.Opportunity', verbose_name='Возможности')),
            ],
            options={
                'verbose_name': 'Начало',
                'verbose_name_plural': 'Начало',
            },
        ),
        migrations.CreateModel(
            name='StandZone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_title', models.CharField(max_length=300, verbose_name='Заглавный текст')),
                ('block_description', models.TextField(verbose_name='Описание')),
                ('subtext', models.CharField(max_length=300, verbose_name='Текст об окончании бронирования')),
                ('photo', models.ManyToManyField(to='trade_zone.StandPhoto', verbose_name='Фото Стендов')),
            ],
            options={
                'verbose_name': 'Зона Стенда',
                'verbose_name_plural': 'Зона Стенда',
            },
        ),
        migrations.CreateModel(
            name='Stand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
                ('number_of_places', models.PositiveIntegerField(verbose_name='Кол-во мест')),
                ('size', models.CharField(max_length=300, verbose_name='Размер')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='Цена')),
                ('additionally', models.ManyToManyField(to='trade_zone.Additionally', verbose_name='Дополнительно')),
                ('decor', models.ManyToManyField(to='trade_zone.Decor', verbose_name='Оформление')),
            ],
            options={
                'verbose_name': 'Стенд',
                'verbose_name_plural': 'Стенды',
            },
        ),
    ]
