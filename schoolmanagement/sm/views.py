from django.http import request, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Student
from .forms import *


# Create your views here.
class StudentListView(View):
    def get(self, request, *args, **kwargs):
        form = StudentCreateForm
        value = Student.objects.all()
        return render(request, 'student.html', {'form': form, 'value': value})

    def post(self, request, *args, **kwargs):
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("studentlist")


class StudentUpdateView(View):
    def get(self, request, pk):
        data = get_object_or_404(Student, id=pk)
        form = StudentUpdateForm(instance=data)
        context = {
            "form": form
        }
        return render(request, "updatestudent.html", context)

    def post(self, request, pk):
        data = get_object_or_404(Student, id=pk)
        form = StudentUpdateForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('studentlist')
        context = {
            "form": form
        }
        return render(request, "updatestudent.html", context)


class StudentDeleteView(View):
    def get(self, request, pk):
        member = Student.objects.get(id=pk)
        member.delete()
        return redirect('studentlist')


class TeacherListView(View):
    def get(self, request, *args, **kwargs):
        form = TeacherCreateForm
        value = Teacher.objects.all()
        return render(request, 'teacher.html', {'form': form, 'value': value})

    def post(self, request, *args, **kwargs):
        form = TeacherCreateForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("teacherlist")


class TeacherUpdateView(View):
    def get(self, request, pk):
        data = get_object_or_404(Teacher, id=pk)
        form = TeacherUpdateForm(instance=data)
        context = {
            "form": form
        }
        return render(request, "updateteacher.html", context)

    def post(self, request, pk):
        data = get_object_or_404(Teacher, id=pk)
        form = TeacherUpdateForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('teacherlist')
        context = {
            "form": form
        }
        return render(request, "updateteacher.html", context)


class TeacherDeleteView(View):
    def get(self, request, pk):
        member = Teacher.objects.get(id=pk)
        member.delete()
        return redirect('teacherlist')


class SectionListView(View):
    def get(self, request, *args, **kwargs):
        form = SectionCreateForm
        value = Section.objects.all()
        return render(request, 'section.html', {'form': form, 'value': value})

    def post(self, request, *args, **kwargs):
        form = SectionCreateForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("sectionlist")


class SectionUpdateView(View):
    def get(self, request, pk):
        data = get_object_or_404(Student, id=pk)
        form = SectionUpdateForm(instance=data)
        context = {
            "form": form
        }
        return render(request, "updatesection.html", context)

    def post(self, request, pk):
        data = get_object_or_404(Student, id=pk)
        form = SectionUpdateForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('sectionlist')
        context = {
            "form": form
        }
        return render(request, "updatesection.html", context)


class SectionDeleteView(View):
    def get(self, request, pk):
        member = Section.objects.get(id=pk)
        member.delete()
        return redirect('sectionlist')


class SubjectListView(View):
    def get(self, request, *args, **kwargs):
        form = SubjectCreateForm
        value = Subject.objects.all()
        return render(request, 'subject.html', {'form': form, 'value': value})

    def post(self, request, *args, **kwargs):
        form = SubjectCreateForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("subjectlist")


class SubjectDeleteView(View):
    def get(self, request, pk):
        item = Subject.objects.get(id=pk)
        item.delete()
        return redirect('subjectlist')
