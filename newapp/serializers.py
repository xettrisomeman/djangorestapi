from rest_framework import serializers


from .models import (
    Theory,
    Scientist
)


class TheorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Theory
        fields = ('id' , 'name','created' , 'based_on' , 'details' ,'related_url')


class ScientistSerializer(serializers.ModelSerializer):
    theories = TheorySerializer(many=True)
    class Meta:
        model = Scientist
        fields = ('id','first_name' , 'last_name' , 'date_of_birth' , 'birth_place' , 'death','theories')

