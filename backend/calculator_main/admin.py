from django.contrib import admin

from .models import User, CitiesTemplate, MailingType, UrlsContentMail, UrlsContentTransfer, \
    ListAllUrls

admin.site.register(User)
admin.site.register(CitiesTemplate)
admin.site.register(MailingType)
admin.site.register(UrlsContentMail)
admin.site.register(UrlsContentTransfer)
admin.site.register(ListAllUrls)
