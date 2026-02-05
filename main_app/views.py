from django.shortcuts import render

def student_form(request):
    return render(request, 'form.html')