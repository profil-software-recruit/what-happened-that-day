import calendar
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Date(models.Model):
    month = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    month_name = models.CharField(max_length=9)
    day = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(31)])
    fact = models.CharField(max_length=1000)

    def save(self, *args, **kwargs):
        self.month_name = calendar.month_name[self.month]
        super().save(*args, **kwargs)
