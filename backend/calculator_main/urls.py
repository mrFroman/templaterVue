from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import ListAllUrlsApiView, CitiesTemplateApiView, UserLoginAPIView, UserRegisterationAPIView, \
    UserLogoutAPIView, UrlsContentMailApiView, UserAPIView, PostUrlContentApiView

router = routers.DefaultRouter()
# router.register(r'postdate', ListAllUrlsApiView, basename='postdate')    # API информации о рассылке
router.register(r'cities', CitiesTemplateApiView, basename='cities')     # Информация о городе и о рассылке
router.register(r'content', UrlsContentMailApiView, basename='content')  # информация о мероприятии (не перенос)
# router.register(r'posturl', PostUrlContentApiView.as_view(), basename='posturl')


urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegisterationAPIView.as_view(), name='create-user'),
    path('login/', UserLoginAPIView.as_view(), name='login-user'),
    path('logout/', UserLogoutAPIView.as_view(), name='logout-user'),
    path('posturl/', PostUrlContentApiView.as_view(), name='posturl'),
    path('postdate/', ListAllUrlsApiView.as_view(), name='postdate'),
    path('user/', UserAPIView.as_view(), name='user'),          # активный пользователь на данный момент
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
