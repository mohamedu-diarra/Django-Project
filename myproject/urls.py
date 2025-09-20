from django.urls import path
from . import views

urlpatterns = [
    path("", views.student_list, name="student_list"),
    path("student/<int:pk>/", views.student_detail, name="student_detail"),
    path("add/", views.add_student, name="add_student"),
    path("edit/<int:pk>/", views.edit_student, name="edit_student"),
    path("delete/<int:pk>/", views.delete_student, name="delete_student"),
]