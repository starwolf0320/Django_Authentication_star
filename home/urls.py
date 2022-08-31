from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django_otp.admin import OTPAdminSite
from allauth.account.views import confirm_email
from django.conf.urls import url


urlpatterns = [
    path('auth/', include('djoser.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^account/', include('allauth.urls')),
    url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('allauth.urls')),
    
    path('secret-admin/', admin.site.urls),
    path('', include('accounts.urls', namespace='columns'))
    # re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]

if not settings.DEBUG:
    admin.site.__class__ = OTPAdminSite
admin.site.site_title = "Django Security Tutorial"
admin.site.site_header = "Django Security Tutorial"
