from django.db import models
from django.db.models import JSONField


class StockData(models.Model):
    stock_symbol = models.CharField(max_length=10)
    opening_price = models.DecimalField(max_digits=20, decimal_places=15)  # Increased max_digits
    closing_price = models.DecimalField(max_digits=20, decimal_places=15)  # Increased max_digits
    high = models.DecimalField(max_digits=20, decimal_places=15)  # Increased max_digits
    low = models.DecimalField(max_digits=20, decimal_places=15)  # Increased max_digits
    volume = models.BigIntegerField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.stock_symbol} - {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"


class AdditionalData(models.Model):
    data_type = models.CharField(max_length=50)
    timestamp = models.DateTimeField()
    additional_info = JSONField()

    def __str__(self):
        return f"{self.data_type} - {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
