from django.urls import path
from .views import DataIngestView

urlpatterns = [
    path('', DataIngestView.as_view(), name='data_ingest'),
]
