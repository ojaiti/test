from rest_framework import serializers
from status_farm.models import StatusFarm

class StatusFarmSerializer(serializers.ModelSerializer):

    class Meta:
        model = StatusFarm
        fields = ['name','created_at']
        depth = 1

    