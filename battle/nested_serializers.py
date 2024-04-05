from rest_framework import serializers

from battle.models import Battle


class BattleListPKSerializer(serializers.ModelSerializer):
    monsterA = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )
    monsterB = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )
    winner = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )

    class Meta:
        model = Battle
        fields = "__all__"
