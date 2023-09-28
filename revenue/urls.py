from django.urls import path

from spend.views import get_queryset_spend_statistic

urlpatterns = [
    path("", get_queryset_spend_statistic, name="revenue-statistic"),
]

app_name = "revenue"
