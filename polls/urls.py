from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

# TODO-Andrey: внимательнее вставляй куски кода!!!
# urlpatterns = [
#     url(r'^polls/', include('polls.urls')),
#     url(r'^admin/', admin.site.urls),
# ]
