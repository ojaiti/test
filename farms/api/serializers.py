from rest_framework import serializers
from farms.models import Farm

class FarmsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Farm
        fields = ['id','name','id_ref','created_at','is_active','status','region',]
        #depth = 1

    