from rest_framework import serializers
from .models import Course
from contents.serializers import ContentSerializer
from students_courses.serializers import StudentCourseSerializer
from accounts.serializers import AccountSerializer
from accounts.models import Account
from students_courses.models import StudentCourse

# from students_courses.serializers import


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "status",
            "start_date",
            "end_date",
            "instructor",
            "contents",
            "students_courses",
        ]
        extra_kwargs = {
            "contents": {"read_only": True},
            "students_courses": {"read_only": True},
        }


class CourseDetailSerializer(serializers.ModelSerializer):
    instructor = AccountSerializer(read_only=True)
    contents = ContentSerializer(read_only=True, many=True)
    students_courses = StudentCourseSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "status",
            "start_date",
            "end_date",
            "instructor",
            "contents",
            "students_courses",
        ]


class StudentDetaiSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    students_courses = StudentCourseSerializer(many=True)

    class Meta:
        model = Course
        fields = ["id", "name", "students_courses"]

    def update(self, instance, validated_data):
        email_list = []
        for student in validated_data["students_courses"]:
            email = student["student"]["email"]
            try:
                student = Account.objects.get(email=email)
                try:
                    StudentCourse.objects.get(course=instance, student=student)
                except:
                    instance.students.add(student)
                    instance.save()
                return instance
            except Account.DoesNotExist:
                email_list.append(email)
            if email_list:
                raise serializers.ValidationError(
                    {
                        "detail": f"No active accounts was found: {', '.join(email_list)}."
                    }
                )
