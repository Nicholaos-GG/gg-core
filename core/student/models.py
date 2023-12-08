import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)


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
    department = models.CharField(max_length=255, choices=DEPARTMENT_CHOICES)
    sex = models.CharField(choices=[("M", "Male"), ("F", "Female")], max_length=1)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    entry_date = models.DateField(null=True)
    leave_date = models.DateField(null=True)
    spiritual_title = models.CharField(
        max_length=255, null=True, choices=SPIRITUAL_TITLE_CHOICES
    )

    def __str__(self):
        if self.spiritual_title is None:
            return f"{self.first_name} {self.last_name}"
        return f"{self.spiritual_title} {self.first_name} {self.last_name}"
