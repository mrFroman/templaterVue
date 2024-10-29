from django.contrib.auth import get_user_model
from rest_framework import viewsets, status, generics
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from django_filters.rest_framework import DjangoFilterBackend

from .models import ListAllUrls, CitiesTemplate, UrlsContentMail
from .serializers import ListAllUrlsSerializer, CitiesTemplateSerializer, UserRegistrationSerializer, \
    UserLoginSerializer, UserSerializer, UrlsContentMailSerializer, PostUrlContentSerializer
from .services import created_mailing_list

''' Api для моделей шаблонизатора '''


class UserRegisterationAPIView(GenericAPIView):
    """
    An endpoint for the client to create a new User.
    """

    User = get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = RefreshToken.for_user(user)
        data = serializer.data
        data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return Response(data, status=status.HTTP_201_CREATED)


class UserLoginAPIView(GenericAPIView):
    """
    An endpoint to authenticate existing users using their email and password.
    """
    # User = get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data
            serializer = UserSerializer(user)
            token = RefreshToken.for_user(user)
            data = serializer.data
            data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLogoutAPIView(GenericAPIView):
    """
    An endpoint to logout users.
    """
    User = get_user_model()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTTokenUserAuthentication,)

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserAPIView(RetrieveUpdateAPIView):
    """
    Get, Update user information
    """
    serializer_class = UserSerializer
    User = get_user_model()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTTokenUserAuthentication,)

    def get_object(self):
        return self.request.user


# class ListAllUrlsApiView(viewsets.ModelViewSet):
class ListAllUrlsApiView(generics.ListCreateAPIView):
    queryset = ListAllUrls.objects.all()
    serializer_class = ListAllUrlsSerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (JWTTokenUserAuthentication,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            new_template = serializer.save()
            return Response(new_template.id, status=status.HTTP_200_OK)
        else:
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)


class CitiesTemplateApiView(viewsets.ModelViewSet):
    queryset = CitiesTemplate.objects.all()
    serializer_class = CitiesTemplateSerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (JWTTokenUserAuthentication,)


class UrlsContentMailApiView(viewsets.ModelViewSet):
    queryset = UrlsContentMail.objects.all()
    serializer_class = UrlsContentMailSerializer
    permission_classes = (AllowAny, )   # (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_created']


class PostUrlContentApiView(GenericAPIView):
    serializer_class = PostUrlContentSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            url = serializer.data['url']
            content = created_mailing_list(url)
            return Response(content, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

