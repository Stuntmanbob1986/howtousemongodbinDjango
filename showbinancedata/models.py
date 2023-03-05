from django.db import models

# example for a class based view


class binanceData(models.Model):
    COINPAIRS = [
        ('AVAX/EUR', 'AVAX/EUR'),
        ('BTC/EUR', 'BTC/EUR'),
        ('ETH/EUR', 'ETH/EUR'),
    ]
    ACCURACYS = [
        ('d', 'day'),
        ('h', 'hour'),
    ]

    coinpair = models.CharField(max_length=20, choices=COINPAIRS)
    accuracy = models.CharField(max_length=20, choices=ACCURACYS)
    start = models.DateField()
    end = models.DateField()

