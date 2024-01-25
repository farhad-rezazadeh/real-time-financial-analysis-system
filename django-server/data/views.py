from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import StockData
from .serializers import AdditionalDataSerializer, StockDataSerializer
from .utils import send_to_kafka


class DataIngestView(APIView):
    def post(self, request, format=None):
        data = request.data.copy()
        if 'data_type' in data:
            # Handle AdditionalData
            topic = "additional_data"
            serializer = AdditionalDataSerializer(data=data)
        else:
            # Handle StockData
            topic = "stock_data"
            serializer = StockDataSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            send_to_kafka(topic, request.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StockDataRetrieveView(APIView):
    def get(self, request, format=None):
        stock_symbol = request.query_params.get('stock_symbol')

        if stock_symbol:
            queryset = StockData.objects.filter(stock_symbol=stock_symbol)
        else:
            queryset = StockData.objects.all()

        serializer = StockDataSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)