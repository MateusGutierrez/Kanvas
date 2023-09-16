from . import views
from django.urls import path

urlpatterns = [
    path("courses/<course_id>/contents/", views.ContentView.as_view()),
    path(
        "courses/<course_id>/contents/<content_id>/",
        views.CourseContentDetailView.as_view(),
    ),
]
