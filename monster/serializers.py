from rest_framework import serializers

from monster.models import Monster


class MonsterFileSerializer(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = Monster
        fields = "__all__"
