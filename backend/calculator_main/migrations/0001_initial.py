# Generated by Django 4.2.1 on 2024-01-10 06:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(db_index=True, max_length=50, unique=True, verbose_name='Почтовый адрес')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='CitiesTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города шаблонизатора',
            },
        ),
        migrations.CreateModel(
            name='ListAllUrls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create_mail', models.DateField(verbose_name='Дата рассылки')),
                ('date_update_mail', models.DateField(verbose_name='Дата обновления')),
                ('paid_mailing', models.BooleanField(default=False, verbose_name='Платная рассылка')),
                ('agreement', models.CharField(max_length=300, null=True, verbose_name='Необходимо согласовать')),
                ('date_departure', models.DateField(verbose_name='Дата отправки')),
                ('client_base', models.TextField(null=True, verbose_name='База отправки')),
                ('city_mail', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='list_city', to='calculator_main.citiestemplate', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Данные для рассылки',
                'verbose_name_plural': 'Данные для рассылок',
            },
        ),
        migrations.CreateModel(
            name='MailingType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail_type', models.CharField(max_length=30, verbose_name='Вид рассылки')),
            ],
            options={
                'verbose_name': 'Вид рассылки',
                'verbose_name_plural': 'Виды рассылок',
            },
        ),
        migrations.CreateModel(
            name='UrlsContentTransfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_phone_links', models.CharField(max_length=30, verbose_name='Ссылка на телефон')),
                ('number_phone', models.CharField(max_length=30, verbose_name='Номер телефона')),
                ('alert_date', models.CharField(max_length=10, verbose_name='Дата переноса')),
                ('labels', models.CharField(max_length=300, verbose_name='UTM-метки')),
                ('pixels', models.CharField(max_length=300, verbose_name='Пиксель')),
                ('key', models.CharField(max_length=300, verbose_name='Ключ рассылки')),
                ('social', models.CharField(max_length=300, verbose_name='Соцсети')),
                ('id_created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator_main.listallurls', verbose_name='id рассылки')),
            ],
            options={
                'verbose_name': 'Информация о переносе',
                'verbose_name_plural': 'Содержимое ссылки для переноса',
            },
        ),
        migrations.CreateModel(
            name='UrlsContentMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(db_index=True, verbose_name='Ссылка на мероприятие')),
                ('description', models.TextField(verbose_name='Описание мероприятия')),
                ('category', models.CharField(max_length=20, verbose_name='Категория мероприятия')),
                ('title', models.CharField(max_length=30, verbose_name='Название мероприятия')),
                ('rate', models.CharField(max_length=3, verbose_name='Ценз')),
                ('date', models.CharField(max_length=10, verbose_name='Дата мероприятия')),
                ('time', models.CharField(max_length=10, verbose_name='Время мероприятия')),
                ('venue', models.CharField(max_length=30, verbose_name='Площадка')),
                ('price', models.CharField(max_length=15, verbose_name='Цена')),
                ('is_pushkin_card', models.BooleanField()),
                ('image', models.ImageField(upload_to='calculator_main/img', verbose_name='Афиша')),
                ('id_created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator_main.listallurls', verbose_name='id рассылки')),
            ],
            options={
                'verbose_name': 'Информация о мероприятии',
                'verbose_name_plural': 'Мероприятия для рассылки',
            },
        ),
        migrations.AddField(
            model_name='listallurls',
            name='type_mail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='list_mail_type', to='calculator_main.mailingtype', verbose_name='Вид рассылки'),
        ),
        migrations.AddField(
            model_name='listallurls',
            name='user_create',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='list_user', to=settings.AUTH_USER_MODEL, verbose_name='Создатель рассылки'),
        ),
    ]
