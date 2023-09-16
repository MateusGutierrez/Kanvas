from django.db import models
import uuid


# Create your models here.
class STUDENT_COURSE_STATUS(models.TextChoices):
    pending = "pending"
    accepted = "accepted"


class StudentCourse(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    status = models.CharField(
        max_length=8,
        choices=STUDENT_COURSE_STATUS.choices,
        default=STUDENT_COURSE_STATUS.pending,
    )
    course = models.ForeignKey(
        "courses.Course", on_delete=models.CASCADE, related_name="students_courses"
    )
    student = models.ForeignKey(
        "accounts.Account", on_delete=models.CASCADE, related_name="students_courses"
    )
