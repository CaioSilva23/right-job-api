from rest_framework import serializers
from ..models import Tecnologia

class TecnologiaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tecnologia
        fields = ('id','nome',)
        