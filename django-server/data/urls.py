from django.urls import path

from .views import DataIngestView, StockDataRetrieveView, view_chart

app_name = 'data'

urlpatterns = [
    path('ingest/', DataIngestView.as_view(), name='ingest'),
    path('stock-data/', StockDataRetrieveView.as_view(), name='stock-data-retrieve'),
    path('view-chart/', view_chart, name='view'),
    path('view-chart/<str:stock_symbol>/', view_chart, name='view-chart'),
]
