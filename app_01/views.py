from django.shortcuts import render
from rest_framework import viewsets
from .models import Student, Group
from .serializer import StudentSerializer, GroupSerializer


# Create your views here.

class StudentViewsSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
