from django.db import models


class FinDataModel(models.Model):
    fd_name = models.CharField(blank=False, max_length=10)
    fd_date = models.DateField()
    fd_open = models.DecimalField(max_digits=12, decimal_places=2)
    fd_high = models.DecimalField(max_digits=12, decimal_places=2)
    fd_low = models.DecimalField(max_digits=12, decimal_places=2)
    fd_close = models.DecimalField(max_digits=12, decimal_places=2)
    fd_volume = models.IntegerField()
