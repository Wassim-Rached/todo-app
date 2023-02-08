from django.contrib import admin
from django.urls import path,include,re_path
from .schemas import schema_view
from rest_framework.response import Response 
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    #health_check
    path('',views.HelloApiView.as_view(),name='health_check'),
    #swagger api
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]