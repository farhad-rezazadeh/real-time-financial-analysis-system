from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import send_to_kafka


class DataIngestView(APIView):
    def post(self, request, format=None):
        data = request.data
        # Determine the topic based on data type or any other logic
        topic = 'stock_data' if 'data_type' not in data else 'additional_data'
        send_to_kafka(topic, data)
        return Response({"message": "Data sent to Kafka topic: {}".format(topic)}, status=status.HTTP_200_OK)
