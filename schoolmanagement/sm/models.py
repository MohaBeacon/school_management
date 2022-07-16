from django.db import models

# Create your models here.
from django.urls import reverse


class Section(models.Model):
    standard_name = models.CharField(max_length=20)
    section_name = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.standard_name + "-" + self.section_name


class Subject(models.Model):
    subject_name = models.CharField(max_length=20)

    def __str__(self):
        return self.subject_name


class Student(models.Model):
    student_name = models.CharField(max_length=200)
    roll_no = models.CharField(max_length=100)
    std = models.ForeignKey(Section, on_delete=models.CASCADE, null=True, blank=False)

    def __str__(self):
        return self.roll_no



class Teacher(models.Model):
    teacher_name = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    std = models.ForeignKey(Section, on_delete=models.CASCADE, null=True, blank=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=False)

    def __str__(self):
        return self.teacher_name + " " + self.degree
