# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from decimal import Decimal
from django.conf import settings
from django.core.validators import MinValueValidator

User = settings.AUTH_USER_MODEL

# Create your models here.
class transfer(models.Model):
    sender = models.ForeignKey(
        User,
        related_name='send',
        on_delete=models.CASCADE,
    )
    receiver = models.ForeignKey(
        User,
        related_name='receive',
        on_delete=models.CASCADE,
    )
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        validators=[
            MinValueValidator(Decimal('10.00'))
        ]
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.sender)
