from student.models import *
from student.serializers import *
from rest_framework import viewsets, filters
from rest_framework.views import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.permissions import AllowAny


class StudentViewSet(viewsets.ModelViewSet):
    http_method_names = ("get", "post")
    permission_classes = (AllowAny,)
    serializer_class = StudentSerializer

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
