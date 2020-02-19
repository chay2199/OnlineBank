from django.conf.urls import url
from .views import transfer_fund
from .views import foreign_fund

urlpatterns = [
    url(r'^transfer/$', transfer_fund, name='fund_transfer'),
    url(r'^ftransfer/$', foreign_fund, name='foreign_fund'),
]