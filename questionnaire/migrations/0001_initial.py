# Generated by Django 5.0.4 on 2024-05-01 20:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название ответа')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название вопроса')),
                ('description', models.TextField(blank=True, max_length=255, verbose_name='Описание')),
                ('answer', models.ManyToManyField(blank=True, related_name='answers', to='questionnaire.answer', verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название опросника')),
                ('question', models.ManyToManyField(related_name='questions', to='questionnaire.question', verbose_name='Вопрос')),
            ],
            options={
                'verbose_name': 'Опрос',
                'verbose_name_plural': 'Опросы',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Имя владельца')),
                ('surname', models.CharField(blank=True, max_length=50, verbose_name='Фамилия владельца')),
                ('company', models.CharField(max_length=50, verbose_name='Название компании')),
                ('address', models.CharField(max_length=50, verbose_name='Адрес компании')),
                ('direction', models.CharField(choices=[('bar', 'Бар'), ('restaurant', 'Ресторан'), ('cafe', 'Кафе'), ('other', 'Другое')], max_length=20)),
                ('is_new', models.BooleanField(default=False, verbose_name='Новая ли компания')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emails', to='questionnaire.user', verbose_name='Почта владельца')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
    ]