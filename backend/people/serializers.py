from rest_framework import serializers
from .models import People

# Using model serializers


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ['id', 'first_name', 'last_name', 'age',
                  'standard', 'division', 'school', 'bio', 'created_at']
