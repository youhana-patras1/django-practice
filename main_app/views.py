from django.shortcuts import render
from .models import Student
def student_list(request):
    # Database se saare students mangwao
    students = Student.objects.all()
    # Inko HTML page (template) par bhej do
    return render(request, 'student.html', {'students': students})