"""bankingsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from core.views import home, about,GeneratePdf


urlpatterns = [
    # admin
    url(r'^super_secret/', admin.site.urls),
    # Accounts
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    # core
    url(r'^$', home, name='home'),
    url(r'^about/$', about, name='about'),
    url(r'^GeneratePdf/$', GeneratePdf, name='GeneratePdf'),
    # transactions
    url(r'^', include('transactions.urls', namespace='transactions')),
    #transfers
    url(r'^', include('transfer.urls', namespace='transfer')),
    #adminMask
    url(r'^',include('adminMask.urls',namespace='adminMask')),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
        )
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
        )
