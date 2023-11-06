from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="public_id", read_only=True, format="hex")

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
