# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

def student_list(request):
    students = Student.objects.all()
    search_query = request.GET.get("q")
    if search_query:
        students = students.filter(name__icontains=search_query)
    return render(request, "studentsapp/student_list.html", {"students": students})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, "studentsapp/student_detail.html", {"student": student})

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm()
    return render(request, "studentsapp/student_form.html", {"form": form})

def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm(instance=student)
    return render(request, "studentsapp/student_form.html", {"form": form})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect("student_list")
    return render(request, "studentsapp/student_confirm_delete.html", {"student": student})