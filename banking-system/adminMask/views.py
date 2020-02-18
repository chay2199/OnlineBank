
from __future__ import unicode_literals

from django.shortcuts import render
from ipaddr import client_ip

def admin_res(request):
	return render(request,"req_res.html")


def get_ip(request):
    ipaddr = client_ip(request)
    print("Public IP address of intruder is:")
    print(ipaddr)
    return render(request, "fakelogin.html")