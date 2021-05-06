from rest_framework import serializers
from .models import FinDataModel


class FinDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinDataModel
        fields = [
            "id",
            "fd_name",
            "fd_date",
            "fd_open",
            "fd_high",
            "fd_low",
            "fd_close",
            "fd_volume",
        ]
