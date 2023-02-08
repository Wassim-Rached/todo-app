from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = Item
		fields = '__all__'
