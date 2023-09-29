from django.db.models import Sum
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from spend.models import SpendStatistic


class SpendStatisticView(APIView):
    def get(self, request: Request) -> Response:
        queryset = SpendStatistic.objects.values("date", "name").annotate(
            total_spend=Sum("spend"),
            total_impressions=Sum("impressions"),
            total_clicks=Sum("clicks"),
            total_conversion=Sum("conversion"),
            total_revenue=Sum("revenues__revenue"),
        )

        return Response(queryset, status=status.HTTP_200_OK)
