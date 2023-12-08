from student.models import *
from student.serializers import *
from student.filters import *
from student.permissions import *
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class StudentViewSet(viewsets.ModelViewSet):
    http_method_names = ("get", "post", "patch", "delete")
    queryset = Student.objects.all()
    permission_classes = (DjangoModelPermissions,)
    serializer_class = StudentSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ["first_name", "last_name"]
    ordering_fields = [
        "first_name",
        "last_name",
        "spiritual_title",
        "entry_date",
        "leave_date",
    ]
    filterset_class = StudentFilter

    def get_serializer_context(self):
        return {"request": self.request}
