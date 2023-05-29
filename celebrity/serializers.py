from rest_framework import serializers

from celebrity.models import Celebrity


class CelebritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Celebrity
        fields = '__all__'
