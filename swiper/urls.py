
from django.conf.urls import url
from django.contrib import admin

from user import api as api_user

urlpatterns = [
    # url(r'^admin/', admin.site.urls)
    url(r'^api/user/vcode$', api_user.get_verify_code),
    url(r'^api/user/login$', api_user.login),
    url(r'^api/user/profile/shows$', api_user.show_profile),
    url(r'^api/user/profile/modify$', api_user.modify_profile),
    url(r'^api/user/avatar/upload$', api_user.upload_avatar)
]
