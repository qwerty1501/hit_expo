# Generated by Django 3.2.9 on 2023-07-29 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_organic', models.CharField(max_length=128, verbose_name='Название организации')),
                ('surname', models.CharField(max_length=16, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=16, verbose_name='Имя')),
                ('email', models.EmailField(max_length=32, verbose_name='E-mail')),
                ('number', models.CharField(max_length=16, verbose_name='Телефон')),
                ('user_status', models.CharField(blank=True, choices=[['Партнер', 'Партнер'], ['Участник', 'Участник'], ['Сми', 'Сми'], ['Спонсор', 'Спонсор']], default=None, max_length=100, null=True, verbose_name='Выберите направление')),
                ('data', models.BooleanField(default=False, verbose_name='Я согласен на обработку моих персональных данных')),
            ],
            options={
                'verbose_name': 'ПРЕДВАРИТЕЛЬНАЯ ЗАЯВКА',
                'verbose_name_plural': 'ПРЕДВАРИТЕЛЬНАЯ ЗАЯВКА',
                'db_table': 'application',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Ф.И.О')),
                ('mail', models.EmailField(max_length=300, verbose_name='Почта')),
                ('phone', models.CharField(max_length=300, verbose_name='Номер телефона')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Обратная связь',
                'verbose_name_plural': 'Обратная связь',
                'db_table': 'feedback',
            },
        ),
    ]