from rest_framework import serializers

from main.models import Copch, Poly, Cold


class CopchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Copch
        fields = "__all__"

class PolySerializer(serializers.ModelSerializer):
    class Meta:
        model = Poly
        fields = "__all__"

class ColdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cold
        fields = "__all__"