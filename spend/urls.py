from django.urls import path

from spend.views import get_queryset_spend_statistic

urlpatterns = [
    path("", get_queryset_spend_statistic, name="spend-statistic"),
]

app_name = "spend"
