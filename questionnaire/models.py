from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Profile(models.Model):
    BAR = 'bar'
    RESTAURANT = 'restaurant'
    CAFE = 'cafe'
    OTHER = 'other'

    DIRECTION_CHOICES = [
        (BAR, 'Бар'),
        (RESTAURANT, 'Ресторан'),
        (CAFE, 'Кафе'),
        (OTHER, 'Другое'),
    ]

    name = models.CharField(max_length=50, verbose_name='Имя владельца', blank=True)
    surname = models.CharField(max_length=50, verbose_name='Фамилия владельца', blank=True)
    email = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Почта владельца', related_name='emails')
    company = models.CharField(max_length=50, verbose_name='Название компании')
    address = models.CharField(max_length=50, verbose_name='Адрес компании')
    direction = models.CharField(max_length=20, choices=DIRECTION_CHOICES)
    is_new = models.BooleanField(default=False, verbose_name='Новая ли компания')

    def __str__(self):
        return f'{self.company}-{self.email}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Answer(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название ответа')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class Question(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название вопроса')
    description = models.TextField(max_length=255, blank=True, verbose_name='Описание')
    answer = models.ManyToManyField(Answer, verbose_name='Ответ', related_name='answers', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Survey(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название опросника')
    question = models.ManyToManyField(Question, verbose_name='Вопрос', related_name='questions')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'
