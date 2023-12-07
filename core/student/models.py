import uuid
from django.db import models
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import AbstractUser


class Student(models.Model):
    DEPARTMENT_CHOICES = [
        ("CSE", "Computer Science and Engineering"),
        ("ME", "Mechanical Engineering"),
        ("SE", "Software Engineering"),
        ("CE", "Chemical Engineering"),
    ]
    SPIRITUAL_TITLE_CHOICES = [("Dn", "Deacon"), ("Kes", "Kesis")]
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
    spiritual_title = models.CharField(
        max_length=255, null=True, choices=SPIRITUAL_TITLE_CHOICES
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
