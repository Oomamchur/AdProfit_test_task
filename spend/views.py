from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from spend.models import SpendStatistic


@api_view(["GET"])
def get_queryset_spend_statistic(request: Request) -> Response:
    queryset = SpendStatistic.objects.all()

    response_message = f"Number of likes in period"

    return Response(queryset, status=status.HTTP_200_OK)
