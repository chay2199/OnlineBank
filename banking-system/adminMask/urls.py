from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^admin/$', views.get_ip, name='admin'),
	url(r'^admin_res/$', views.admin_res, name='admin_res'),
]