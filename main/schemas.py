from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="TODO APP API",
      default_version='v1',
      description="todo app api with swagger documentation",
      contact=openapi.Contact(email="wassimrached404@gmail.com"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
