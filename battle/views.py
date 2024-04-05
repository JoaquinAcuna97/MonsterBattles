from django.db import transaction
from django.http import Http404
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from battle.models import Battle
from battle.nested_serializers import BattleListPKSerializer
from battle.serializers import BattleCreateSerializer
from rest_framework.decorators import action

# Create your views here.
class BattleListCreateView(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    A simple ViewSet for listing battles.
    """

    queryset = Battle.objects.all()
    serializer_class = BattleListPKSerializer
    serializer_create_class = BattleCreateSerializer
    pagination_class = None
    authentication_classes = []
    permission_classes = []

    def get_serializer_class(self):
        if self.action == "create":
            return self.serializer_create_class
        return self.serializer_class


class BattleRetrieveDeleteView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    A simple ViewSet for update, retrieve and delete battles.
    """

    queryset = Battle.objects.all()
    serializer_class = BattleListPKSerializer
    authentication_classes = []
    permission_classes = []

    @transaction.atomic
    def retrieve(self, request, *args, **kwargs):
        try:
            return super(BattleRetrieveDeleteView, self).retrieve(
                request, *args, **kwargs
            )
        except Http404:
            raise Battle.DoesNotExist

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        battle = self.get_object()
        battle.start()
        return Response({'status': 'Battle Started'})


