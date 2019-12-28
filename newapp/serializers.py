from rest_framework import serializers


from .models import (
    Theory,
    Scientist
)


class TheorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Theory
        fields = "__all__"


class ScientistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scientist
        fields = "__all__"

