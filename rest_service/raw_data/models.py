from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=96, unique=False, blank=True)
    last_name = models.CharField(max_length=96, unique=False, blank=True)
    email = models.EmailField(max_length=96, unique=False, blank=True)
    year = models.IntegerField(choices=(
        (1,1),(2,2),(3,3),(4,4),(5,5),(6,6)
    ))
    budget = models.BooleanField(default=True, help_text=("Show is student paid for courses. Allows us to calculate price for future"))


    def __str__(self):
        return "Student [ {}, {} ]".format(self.last_name, self.email)


class Subject(models.Model):
    name = models.CharField(max_length=96, unique=True,blank=True)
    credit = models.FloatField(unique=False,blank=True)
    semester = models.IntegerField(unique=False,blank=True)
    teacher = models.CharField(max_length=96, unique=False, blank=False)


    INFORMATICA = "INFORMATICA"
    BIOLOGY = "BIOLOGY"
    POLITOLOGY = "POLYTOLOGY"


    NAMES_OF_FACULTIES = (
        (INFORMATICA, "INFORMATICA"),
        (BIOLOGY, "BIOLOGY"),
        (POLITOLOGY, "POLITOLOGY"),

    )
    faculty_id = models.CharField(max_length=50, choices=NAMES_OF_FACULTIES)

    def __str__(self):
        return "Subject [ {}, {} ]".format(self.name, self.credit)



class Class(models.Model):
    name = models.CharField(max_length=96, unique=True,blank=True)
    stud_id = models.ForeignKey(Student)
    subj_id = models.ForeignKey(Subject)
    enrolment_date = models.TimeField(auto_now=True)
