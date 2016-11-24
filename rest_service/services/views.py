from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from raw_data.views import Class,Student, Subject


def index(request):
	return HttpResponse("You are in Services index")


@api_view(['GET'])
def enroll(request, format=None):
	print ("********")
	class_id = Class.objects.get(request.content_params['class_id'])
	student_id = Student.objects.get(request.content_params['student_id'])
	subject_id = Subject.objects.get(request.content_params['subject_id'])




