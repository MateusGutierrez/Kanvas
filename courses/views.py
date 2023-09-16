from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)
from .permissions import IsSuper, IsSuperAndAuthenticated, IsCourseOwner
from .models import Course
from .serializers import CourseSerializer, CourseDetailSerializer
from courses.serializers import StudentDetaiSerializer
from django.shortcuts import get_object_or_404
from accounts.models import Account
from rest_framework.exceptions import NotFound


# Create your views here.
class CourseView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuper]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsCourseOwner]
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    lookup_url_kwarg = "course_id"


class StudentViews(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperAndAuthenticated]
    queryset = Course.objects.all()
    serializer_class = StudentDetaiSerializer
    lookup_url_kwarg = "course_id"
    http_method_names = ["get", "put"]


class StudentDetailView(DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperAndAuthenticated]
    queryset = Course.objects.all()
    serializer_class = StudentDetaiSerializer
    lookup_url_kwarg = "course_id"

    def perform_destroy(self, instance):
        student = get_object_or_404(Account, pk=self.kwargs["student_id"])
        student_list = instance.students.all()
        if student not in student_list:
            raise NotFound({"detail": "this id is not associated with this course."})
        instance.students.remove(student)
