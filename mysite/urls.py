from django.contrib import admin
from django.urls import path, include

#from . import views просто 


urlpatterns = [
    # url(r'^$', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
]
