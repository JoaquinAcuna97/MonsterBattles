import csv
import codecs

from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from django.db import transaction
from django.http import Http404

from monster.models import Monster
from monster.nested_serializers import MonsterListRetrieveUpdateSerializer
from monster.serializers import MonsterFileSerializer


# Create your views here.


class MonsterListCreateView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    A simple ViewSet for creating monsters.
    """

    queryset = Monster.objects.all().order_by("name")
    serializer_class = MonsterListRetrieveUpdateSerializer
    pagination_class = None
    authentication_classes = []
    permission_classes = []

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        return super(MonsterListCreateView, self).create(request, *args, **kwargs)

    @transaction.atomic
    def list(self, request):
        queryset = Monster.objects.all()
        serializer = MonsterListRetrieveUpdateSerializer(queryset, many=True)
        return Response(serializer.data)

class MonsterUpdateRetrieveDeleteView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """
    A simple ViewSet for update, retrieve and delete monsters.
    """

    queryset = Monster.objects.all().order_by("name")
    serializer_class = MonsterListRetrieveUpdateSerializer
    authentication_classes = []
    permission_classes = []

    @transaction.atomic
    def retrieve(self, request, *args, **kwargs):
        try:
            return super(MonsterUpdateRetrieveDeleteView, self).retrieve(
                request, *args, **kwargs
            )
        except Http404:
            raise Monster.DoesNotExist

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return super(MonsterUpdateRetrieveDeleteView, self).update(
            request, *args, **kwargs
        )

    @transaction.atomic
    def destroy(self, request, *args, **kwargs):
        return super(MonsterUpdateRetrieveDeleteView, self).destroy(
            request, *args, **kwargs
        )


class MonsterImportView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    A simple ViewSet for bulky create Monsters
    """

    queryset = Monster.objects.all()
    serializer_class = MonsterFileSerializer
    pagination_class = None
    authentication_classes = []
    permission_classes = []

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        try:
            serializer_file = self.serializer_class(data=request.data)
            serializer_file.is_valid(raise_exception=True)
            file = serializer_file.validated_data["file"]

            reader = csv.DictReader(codecs.iterdecode(file, "utf-8"), delimiter=",")
            data = list(reader)

            serializer = MonsterListRetrieveUpdateSerializer(data=data, many=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            headers = self.get_success_headers(serializer.data)

            return Response(
                serializer.data, status=status.HTTP_201_CREATED, headers=headers
            )
        except Exception:
            return Response(
                data={"Error": "Insert monsters with valid formats"},
                status=status.HTTP_400_BAD_REQUEST,
            )
