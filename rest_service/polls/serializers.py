from rest_framework import serializers
from models import Subject, Student, Class


class SubjectSerializer(serializers.ModelSerializer):


	class Meta:
		model = Subject
		fields = ('id', 'faculty_id', 'name', 'credit', 'semester', 'teacher')


class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = ('id', 'first_name', 'last_name', 'email', 'year', 'budget')

class ClassSerializer(serializers.ModelSerializer):

	stud_id = StudentSerializer()
	subj_id = SubjectSerializer()

	class Meta:
		model = Class
		fields = ('stud_id', 'subj_id', 'enrolment_date')


# class FacultySerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Faculty
# 		fields = ('id', "name")


