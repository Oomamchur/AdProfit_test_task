from django.urls import path

from revenue.views import RevenueStatisticView

urlpatterns = [
    path("", RevenueStatisticView.as_view(), name="revenue-statistic"),
]

app_name = "revenue"
