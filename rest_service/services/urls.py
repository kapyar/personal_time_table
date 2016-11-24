
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


#API endpoints
urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^api/enroll/$', views.enroll),

 ]


urlpatterns = format_suffix_patterns(urlpatterns)