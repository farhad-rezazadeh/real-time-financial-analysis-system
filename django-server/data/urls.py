from django.urls import path
from .views import DataIngestView, StockDataRetrieveView

app_name = 'data'

urlpatterns = [
    path('ingest/', DataIngestView.as_view(), name='ingest'),
    path('stock-data/', StockDataRetrieveView.as_view(), name='stock-data-retrieve'),
]
