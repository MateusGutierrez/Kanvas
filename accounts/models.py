from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class Account(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=128)
    my_courses = models.ManyToManyField(
        "courses.Course",
        through="students_courses.StudentCourse",
        related_name="students",
    )
