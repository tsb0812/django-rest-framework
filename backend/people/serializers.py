from rest_framework import serializers
from .models import People
from django.contrib.auth.models import User

# Using model serializers


class PeopleSerializer(serializers.ModelSerializer):
    account = serializers.ReadOnlyField(source="account.username")

    class Meta:
        model = People
        fields = [
            "id",
            "first_name",
            "last_name",
            "age",
            "standard",
            "division",
            "school",
            "bio",
            "created_at",
            "account",
        ]


# User serializer
class UserSerializer(serializers.ModelSerializer):
    people = serializers.PrimaryKeyRelatedField(
        many=True, queryset=People.objects.all()
    )

    class Meta:
        model = User
        fields = ["id", "username", "people"]
