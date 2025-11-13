from rest_framework import serializers
from .models import EveNote

class EveNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = EveNote
        fields = '__all__'
