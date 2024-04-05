from rest_framework import serializers

from battle.nested_serializers import BattleListPKSerializer

from monster.base_serializer import MonsterBaseSerializer
from monster.models import Monster


class MonsterListRetrieveUpdateSerializer(MonsterBaseSerializer):
    battles = serializers.SerializerMethodField("get_monster_battles")

    def get_monster_battles(self, obj):
        return BattleListPKSerializer(obj.battlesA.all(), many=True).data

    class Meta:
        model = Monster
        fields = "__all__"
