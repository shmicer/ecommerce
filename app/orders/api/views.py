from rest_framework.generics import ListAPIView
from . import serializers
from orders import models


class OrderListAPIView(ListAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer

