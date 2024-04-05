from django.conf.urls import url

from monster.views import (
    MonsterListCreateView,
    MonsterUpdateRetrieveDeleteView,
    MonsterImportView,
)

app_name = "monster"

urlpatterns = [
    url(
        r"(?P<pk>\d+)",
        MonsterUpdateRetrieveDeleteView.as_view(
            {"put": "update", "get": "retrieve", "delete": "destroy"}
        ),
        name="monster_update_retrieve_delete",
    ),
    url(
        r"import", MonsterImportView.as_view({"post": "create"}), name="monster_import"
    ),
    url(
        r"",
        MonsterListCreateView.as_view({"post": "create", "get": "list"}),
        name="monster_list_create",
    ),
]
