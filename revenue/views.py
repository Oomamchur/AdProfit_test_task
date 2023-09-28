from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from revenue.models import RevenueStatistic


@api_view(["GET"])
def get_queryset_spend_statistic(request: Request) -> Response:
    queryset = RevenueStatistic.objects.all()

    response_message = f"Number of likes in period"

    return Response(response_message, status=status.HTTP_200_OK)
