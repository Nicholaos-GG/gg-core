import uuid
from django.db import models


class Student(models.Model):
    id = models.UUIDField(
        editable=False,
        auto_created=True,
        default=uuid.uuid4,
        db_index=True,
        primary_key=True,
    )
    first_name = models.TextField(max_length=255)
    last_name = models.TextField(max_length=255)
    photo = models.ImageField()
    department = models.TextField()
    sex = models.CharField(
        choices=[
            ("F", "Female"),
            ("M", "Male"),
        ],
        max_length=1,
    )
    phone_number = models.TextField(max_length=10)
    email = models.EmailField(null=True)
    entry_date = models.DateField(null=True)
    leave_date = models.DateField(null=True)
    spiritual_title = models.TextField(max_length=255)
    department = models.TextField(max_length=255)
