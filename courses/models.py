from django.db import models
import uuid


# Create your models here.
class COURSE_STATUS(models.TextChoices):
    not_started = "not started"
    in_progress = "in progress"
    finished = "finished"


class Course(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(
        max_length=11, choices=COURSE_STATUS.choices, default=COURSE_STATUS.not_started
    )
    start_date = models.DateField()
    end_date = models.DateField()
    instructor = models.ForeignKey(
        "accounts.Account",
        null=True,
        on_delete=models.PROTECT,
        related_name="courses",
    )
