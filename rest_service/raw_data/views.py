from django.http import HttpResponse
from rest_framework import generics
from rest_framework.decorators import api_view


from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Student, Subject, Class
from .serializers import StudentSerializer,SubjectSerializer,ClassSerializer



# @api_view(['GET'])
# def index(request, format=None):
# 	print ("********")
# 	return Response({
# 		'students': reverse('students-list', request=request, format=format),
# 		'subjects': reverse('subjects-list', request=request, format=format),
# 		'classes': reverse('classes-list', request=request, format=format),
# 	})

def index(request):
	return HttpResponse("You are in the raw_data index. In this index you could work with each entity"
						"CRUD operations")


class StudentList(generics.ListCreateAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateAPIView):
	# permission_classes = (IsOwnerOrReadOnly,)
	queryset = Student.objects.all()
	serializer_class = StudentSerializer


class SubjectList(generics.ListCreateAPIView):
	queryset = Subject.objects.all()
	serializer_class = SubjectSerializer


class SubjectDetail(generics.RetrieveUpdateAPIView):
	queryset = Subject.objects.all()
	serializer_class = SubjectSerializer


class ClassList(generics.ListCreateAPIView):
	queryset = Class.objects.all()
	serializer_class = ClassSerializer


class ClassDetail(generics.RetrieveUpdateAPIView):
	queryset = Class.objects.all()
	serializer_class = ClassSerializer