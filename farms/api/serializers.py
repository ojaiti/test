from rest_framework import serializers
from farms.models import Farm

class FarmsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Farm
        fields = ['name','created_at','is_active','status','division','region',]

    