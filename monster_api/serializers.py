from .models import Monster
from rest_framework import serializers

class MonsterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Monster
        fields = ['id', 'name', 'height', 'description', 'created_at', 'updated_at']