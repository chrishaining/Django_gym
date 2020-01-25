from django.contrib import admin
from my_gym.models import *

# import sites allows you to change the View Site link in the admin page
from django.contrib.admin import sites

# Register your models here.
admin.site.register(Member)
admin.site.register(Session)
admin.site.register(Instructor)
# reset the View Site link in the admin page (the default is to go to root, which I didn't want)
sites.AdminSite.site_url = '/my_gym/'