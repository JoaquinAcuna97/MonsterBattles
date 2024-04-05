from django.conf.urls import url

from battle.views import BattleListCreateView, BattleRetrieveDeleteView

app_name = "battle"

urlpatterns = [
    url(
        r"(?P<pk>\d+)",
        BattleRetrieveDeleteView.as_view({"get": "retrieve", "put": "update"}),
        name="battle_update_retrieve_delete",
    ),
    url(r"", BattleListCreateView.as_view({"get": "list"}), name="battle_list_create"),
]
