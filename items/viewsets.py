from rest_framework import viewsets,permissions
from .models import Item
from .permissions import IsOwnerOrReadOnly
from .serializers import ItemSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

class ItemViewSet(viewsets.ModelViewSet):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly & (IsOwnerOrReadOnly | permissions.IsAdminUser)]

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

	def partial_update(self, request, *args, **kwargs):
		return super().partial_update(request, *args, **kwargs)

	@action(detail=False, methods=['get'])
	def my_items(self, request):
		items = Item.objects.filter(owner=self.request.user)
		serializer = ItemSerializer(items, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)