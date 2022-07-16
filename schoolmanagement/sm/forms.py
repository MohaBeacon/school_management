from django import forms

from .models import *


class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class TeacherCreateForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class TeacherUpdateForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class SubjectCreateForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'


class SectionCreateForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = '__all__'


class SectionUpdateForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = '__all__'
