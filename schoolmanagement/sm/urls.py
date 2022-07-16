from django.urls import path
from .views import *

urlpatterns = [
    path('student', StudentListView.as_view(), name="studentlist"),
    path('<pk>/studentupdate', StudentUpdateView.as_view(), name="studentupdate"),
    path('<pk>/studentdelete', StudentDeleteView.as_view(), name="studentdelete"),
    path('teacher', TeacherListView.as_view(), name="teacherlist"),
    path('<pk>/teacherupdate', TeacherUpdateView.as_view(), name="teacherupdate"),
    path('<pk>/teacherdelete', TeacherDeleteView.as_view(), name="teacherdelete"),
    path('section', SectionListView.as_view(), name="sectionlist"),
    path('<pk>/sectionupdate', SectionUpdateView.as_view(), name="sectionupdate"),
    path('<pk>/sectiondelete', SectionDeleteView.as_view(), name="sectiondelete"),
    path('subject', SubjectListView.as_view(), name="subjectlist"),
    path('<pk>/subjectdelete', SubjectDeleteView.as_view(), name="subjectdelete"),

]
