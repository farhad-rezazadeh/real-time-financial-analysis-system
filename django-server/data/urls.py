from django.urls import path

from .views import DataIngestView, StockDataRetrieveView, view_chart, stock_list

app_name = 'data'

urlpatterns = [
    path('ingest/', DataIngestView.as_view(), name='ingest'),
    path('stock-data/', StockDataRetrieveView.as_view(), name='stock-data-retrieve'),
    path('view-data/<str:stock_symbol>/', view_chart, name='view-chart'),
    path('stock-list/', stock_list, name='stock-list'),
]
