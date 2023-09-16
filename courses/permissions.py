from rest_framework import permissions
from rest_framework.views import Request, View
from contents.models import Content
from courses.models import Course


class IsSuper(permissions.BasePermission):
    def has_permission(self, req: Request, view: View):
        if req.user.is_authenticated and req.method == permissions.SAFE_METHODS:
            return True
        return req.user.is_superuser


class IsAdminOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Content):
        return request.user.is_superuser or request.user in obj.course.students.all()


class IsSuperAndAuthenticated(permissions.BasePermission):
    def has_permission(self, req: Request, view: View):
        return req.user.is_authenticated and req.user.is_superuser


class IsCourseOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Course):
        return request.user.is_superuser or request.user in obj.students.all()
