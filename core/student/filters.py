from django_filters.rest_framework import FilterSet
from .models import Student

class StudentFilter(FilterSet):
  class Meta:
    model = Student
    fields = {
      'department': ['exact'],
      'sex': ['exact'],
      'spiritual_title':['exact'],
      'entry_date':['exact'],
      'leave_date':['exact']
    }