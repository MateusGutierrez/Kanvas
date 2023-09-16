from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from courses.permissions import IsSuper, IsAdminOrOwner
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import Content
from .serializers import ContentSerializer
from courses.models import Course
from courses.serializers import CourseDetailSerializer
from django.shortcuts import get_object_or_404


# Create your views here.
class ContentView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuper]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    def perform_create(self, serializer):
        course_id = self.kwargs.get("course_id")
        course = get_object_or_404(Course, id=course_id)
        serializer.save(course=course)


class CourseContentDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuper | IsAdminOrOwner]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = "content_id"
