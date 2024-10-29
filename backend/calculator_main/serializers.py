from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import ListAllUrls, CitiesTemplate, User, UrlsContentMail, MailingType

''' сериализаторы для шаблонизатора '''


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer class to serialize CustomUser model.
    """

    class Meta:
        model = User
        fields = ("id", "email")


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer class to serialize registration requests and create a new user.
    """

    class Meta:
        model = User
        fields = ("id", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.Serializer):
    """
    Serializer class to authenticate users with email and password.
    """

    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


class ListAllUrlsSerializer(serializers.ModelSerializer):
    # user_create = serializers.StringRelatedField()
    # type_mail = serializers.StringRelatedField()
    # city_mail = serializers.StringRelatedField()
    user_create = serializers.SlugRelatedField(slug_field='email', queryset=User.objects)
    city_mail = serializers.SlugRelatedField(slug_field='city', queryset=CitiesTemplate.objects)
    type_mail = serializers.SlugRelatedField(slug_field='mail_type', queryset=MailingType.objects)

    class Meta:
        model = ListAllUrls
        fields = ('city_mail', 'date_create_mail', 'date_update_mail', 'user_create', 'type_mail', 'paid_mailing',
                  'agreement', 'date_departure', 'client_base')


class CitiesTemplateSerializer(serializers.ModelSerializer):
    list_city = ListAllUrlsSerializer(many=True)

    class Meta:
        model = CitiesTemplate
        fields = ('id', 'city', 'list_city')


class UrlsContentMailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlsContentMail
        fields = '__all__'


class PostUrlContentSerializer(serializers.Serializer):
    url = serializers.CharField()

