from rest_framework import permissions

class IsMeOrReadOnly(permissions.BasePermission):
	message='only the owner can perform this action'
	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True
		return obj.id == request.user.id