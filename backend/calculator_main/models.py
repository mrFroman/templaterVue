import jwt
from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

''' Модели для шаблонизатора '''


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Почтовый адрес должен быть задан')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields['is_staff'] = False
        extra_fields['is_superuser'] = False
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Почтовый адрес', max_length=50, db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email

    def get_email(self):
        return self.email

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=1)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')

    @property
    def token(self):
        return self._generate_jwt_token()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class CitiesTemplate(models.Model):
    city = models.CharField('Город', max_length=30)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города шаблонизатора'

    def __str__(self):
        return self.city


class MailingType(models.Model):
    mail_type = models.CharField('Вид рассылки', max_length=30)

    class Meta:
        verbose_name = 'Вид рассылки'
        verbose_name_plural = 'Виды рассылок'

    def __str__(self):
        return self.mail_type


class UrlsContentMail(models.Model):
    id_created = models.ForeignKey('ListAllUrls', on_delete=models.CASCADE, verbose_name='id рассылки')
    link = models.URLField('Ссылка на мероприятие', db_index=True)
    description = models.TextField('Описание мероприятия')
    category = models.CharField('Категория мероприятия', max_length=20)
    title = models.CharField('Название мероприятия', max_length=30)
    rate = models.CharField('Ценз', max_length=3)
    date = models.CharField('Дата мероприятия', max_length=10)
    time = models.CharField('Время мероприятия', max_length=10)
    venue = models.CharField('Площадка', max_length=30)
    price = models.CharField('Цена', max_length=15)
    is_pushkin_card = models.BooleanField()
    image = models.ImageField('Афиша', upload_to='calculator_main/img')

    class Meta:
        verbose_name = 'Информация о мероприятии'
        verbose_name_plural = 'Мероприятия для рассылки'

    def __str__(self):
        return self.link


class UrlsContentTransfer(models.Model):
    id_created = models.ForeignKey('ListAllUrls', on_delete=models.CASCADE, verbose_name='id рассылки')
    number_phone_links = models.CharField('Ссылка на телефон', max_length=30)
    number_phone = models.CharField('Номер телефона', max_length=30)
    alert_date = models.CharField('Дата переноса', max_length=10)
    labels = models.CharField('UTM-метки', max_length=300)
    pixels = models.CharField('Пиксель', max_length=300)
    key = models.CharField('Ключ рассылки', max_length=300)
    social = models.CharField('Соцсети', max_length=300)

    class Meta:
        verbose_name = 'Информация о переносе'
        verbose_name_plural = 'Содержимое ссылки для переноса'


class ListAllUrls(models.Model):
    """ общая таблица со всеми связями и просмотр на сайте в виде таблицы """
    city_mail = models.ForeignKey('CitiesTemplate', on_delete=models.PROTECT, verbose_name='Город',
                                  related_name='list_city')
    date_create_mail = models.DateField('Дата рассылки')
    date_update_mail = models.DateField('Дата обновления')

    user_create = models.ForeignKey('User', on_delete=models.PROTECT, verbose_name='Создатель рассылки',
                                    related_name='list_user')
    type_mail = models.ForeignKey('MailingType', on_delete=models.PROTECT, verbose_name='Вид рассылки',
                                  related_name='list_mail_type')
    paid_mailing = models.BooleanField('Платная рассылка', default=False)
    agreement = models.CharField('Необходимо согласовать', max_length=300, null=True)
    date_departure = models.DateField('Дата отправки')
    client_base = models.TextField('База отправки', null=True)

    class Meta:
        verbose_name = 'Данные для рассылки'
        verbose_name_plural = 'Данные для рассылок'

    def __str__(self):
        return "%s: %s, %s" % (self.city_mail, self.type_mail, self.date_create_mail)

