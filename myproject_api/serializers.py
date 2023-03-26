from rest_framework import serializers
from .models import Date


class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = ['id', 'month', 'day', 'fact']


class DateWithMonthNameSerializer(serializers.ModelSerializer):
    month = serializers.CharField(source='month_name')

    class Meta:
        model = Date
        fields = ['id', 'month', 'day', 'fact']


class RankingSerializer(serializers.Serializer):
    month = serializers.CharField(read_only=True, source="month_name")
    month_name = serializers.CharField(write_only=True)
    days_checked = serializers.IntegerField()
