from rest_framework import routers
from . import viewsets 
router = routers.DefaultRouter()

router.register('',viewsets.ItemViewSet,basename='item')
