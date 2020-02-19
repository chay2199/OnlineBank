from django.contrib import admin

from .models import User, AccountDetail, UserAddresse

admin.site.site_header='CASA Bank Admin'
admin.site.register(User)
admin.site.register(AccountDetail)
admin.site.register(UserAddresse)
