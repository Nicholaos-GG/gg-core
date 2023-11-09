from student.models import *
from student.serializers import *
from student.filters import *
from rest_framework import viewsets, filters
from rest_framework.views import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class StudentViewSet(viewsets.ModelViewSet):
    http_method_names = ("get", "post")
    permission_classes = (AllowAny,)
    serializer_class = StudentSerializer

    filter_backends=[SearchFilter, OrderingFilter,DjangoFilterBackend]
    search_fields = ['first_name','last_name']
    ordering_fields = ['first_name','last_name','spiritual_title','entry_date','leave_date']
    filterset_class = StudentFilter    

    def get_queryset(self):
        return Student.objects.all()

    def get_object(self):
        obj = Student.objects.get_object_by_public_id(self.kwargs["pk"])
        return obj

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=HTTP_201_CREATED)
