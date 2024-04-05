from rest_framework import serializers

from battle.models import Battle

from monster.nested_serializers import MonsterListRetrieveUpdateSerializer


class BattleCreateSerializer(serializers.ModelSerializer):
    monsterA = MonsterListRetrieveUpdateSerializer(write_only=True)
    monsterB = MonsterListRetrieveUpdateSerializer(write_only=True)
    winner = MonsterListRetrieveUpdateSerializer(read_only=True)

    class Meta:
        model = Battle
        fields = "__all__"

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        return {}
