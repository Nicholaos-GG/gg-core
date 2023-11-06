from student.models import *
from student.serializers import *
from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny


class StudentViewSet(viewsets.ModelViewSet):
    http_method_names = "get"
    permission_classes = (AllowAny,)
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.all()

    def get_object(self):
        obj = Student.objects.get_object_by_public_id(self.kwargs["pk"])
        return obj
