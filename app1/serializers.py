from rest_framework import serializers
from .models import student

class studentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model=student
        fields='__all__'