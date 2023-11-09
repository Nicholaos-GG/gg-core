import uuid
from django.db import models
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist


class StudentManager(models.Manager):
    def get_object_by_public_id(self, public_id):
        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404


class Student(models.Model):
    public_id = models.UUIDField(
        editable=False,
        default=uuid.uuid4,
        db_index=True,
        unique=True,
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    photo = models.ImageField()
    department = models.CharField(max_length=255)
    sex = models.CharField(choices=[("F", "Female"), ("M", "Male")], max_length=1)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(null=True)
    entry_date = models.DateField(null=True)
    leave_date = models.DateField(null=True)
    spiritual_title = models.CharField(max_length=255, null=True)
    objects = StudentManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
