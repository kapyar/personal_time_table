from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


# API endpoints
urlpatterns = [
	url(r'^$', views.index, name="index"),

	url(r'^api/student/$', views.StudentList.as_view(), name="students-list"),
	url(r'^api/student/(?P<pk>[0-9]+)/$', views.StudentDetail.as_view()),

	url(r'^api/subject/$', views.SubjectList.as_view(), name="subjects-list"),
	url(r'^api/subject/(?P<pk>[0-9]+)/$', views.SubjectDetail.as_view()),

	url(r'^api/class/$', views.ClassList.as_view(), name="classes-list"),
	url(r'^api/class/(?P<pk>[0-9]+)/$', views.ClassDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
