from django.db import models

# Create your models here.
class College(models.Model):
    name = models.CharField(max_length=128)#collegename
    location = models.CharField(max_length=64)
    acronym = models.CharField(max_length=8)
    contact = models.EmailField()

    def __str__(self):
        return self.acronym

class Student(models.Model):
    name = models.CharField(max_length=128)#student name
    dob = models.DateField(null=True,blank = True)
    email = models.EmailField()
    db_folder = models.CharField(max_length=50)
    dropped_out = models.BooleanField(default = False)
    college = models.ForeignKey(College,on_delete=models.CASCADE)
    #backlink to ccollege attribute

    def __str__(self):
        return self.name


class MockTest1(models.Model):
    problem1 = models.IntegerField()
    problem2 = models.IntegerField()
    problem3 = models.IntegerField()
    problem4 = models.IntegerField()
    total = models.IntegerField()
    students = models.OneToOneField(Student,on_delete=models.CASCADE)

    def __str__(self):
        return f"student {self.students.name} marks"



# class testingModel(models.Model):
#     __rollno=models.IntegerField()
#
#     def __str__(self):
#         return self.__rollno


