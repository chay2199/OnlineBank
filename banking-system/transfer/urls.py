from django.conf.urls import url
from .views import transfer_fund

urlpatterns = [
    url(r'^transfer/$', transfer_fund, name='fund_transfer'),
]