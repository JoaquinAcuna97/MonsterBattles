from rest_framework import serializers

from battle.models import Battle

from monster.nested_serializers import MonsterListRetrieveUpdateSerializer
from monster.serializers import MonsterSerializer


class BattleListSerializer(serializers.ModelSerializer):
    monsterA = MonsterListRetrieveUpdateSerializer()
    monsterB = MonsterListRetrieveUpdateSerializer()
    winner = MonsterListRetrieveUpdateSerializer()

    class Meta:
        model = Battle
        fields = "__all__"


class BattleCreateSerializer(serializers.ModelSerializer):
    monsterA = MonsterSerializer(write_only=True)
    monsterB = MonsterSerializer(write_only=True)
    winner = MonsterListRetrieveUpdateSerializer(read_only=True)

    class Meta:
        model = Battle
        fields = "__all__"

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        return {}
