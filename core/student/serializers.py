from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "id",
            "first_name",
            "last_name",
            "photo",
            "department",
            "sex",
            "email",
            "entry_date",
            "leave_date",
            "spiritual_title",
        ]
