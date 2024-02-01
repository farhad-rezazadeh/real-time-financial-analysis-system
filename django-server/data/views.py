from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django_eventstream import send_event

from .models import Stock, StockData
from .serializers import AdditionalDataSerializer, StockDataSerializer, StockSerializer
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
            queryset = StockData.objects.filter(stock__stock_symbol=stock_symbol)
        else:
            queryset = StockData.objects.all()

        serializer = StockDataSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StockRetrieveView(APIView):
    def get(self, request):
        stock_list = Stock.objects.all()
        serializer = StockSerializer(stock_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


def view_chart(request, stock_symbol=None):
    if not stock_symbol:
        try:
            stock_symbol = Stock.objects.first().stock_symbol
        except:
            return HttpResponse("no stock exist")
    return render(request, 'data/chart.html', context={'stock_symbol': stock_symbol})


def change_stock_status(request, stock_symbol):
    try:
        stock = Stock.objects.get(stock_symbol=stock_symbol)
        if request.GET.get('status'):
            stock.status = request.GET.get('status')
            stock.save()
            send_event(
                'notification',
                'stock_status_changed',
                {'stock_symbol': stock_symbol, 'status': stock.status}
            )
            return HttpResponse('stock updated', status=status.HTTP_200_OK)
        else:
            return HttpResponse('please provide stock symbol', status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
        return HttpResponse("not such stock exist", status=status.HTTP_404_NOT_FOUND)
