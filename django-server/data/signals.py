from django.db.models.signals import post_save
from django.dispatch import receiver

from django_eventstream import send_event

from data.models import StockData


@receiver(post_save, sender=StockData)
def post_save_handler(sender, instance, created, **kwargs):
    if created:
        send_event(
            f'stock-{instance.stock_symbol}',
            'stock_updated',
            {'price': instance.opening_price, 'timestamp': str(instance.timestamp)}
        )
