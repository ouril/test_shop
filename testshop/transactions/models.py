from django.db import models
from testshop.models import BaseModel
from django.contrib.auth.models import User

# Create your models here.

class UserBalance(BaseModel):
    user = models.ForeignKey(
        User, 
        related_name='user'
        )
    balance = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0.00,
        verbose_name='user_balance')

    def __str__(self):
        return "Баланс " + self.user.name


class UserBalanceChange(models.Model):
    user = models.ForeignKey(
        User, 
        related_name='balance_changes'
        )
    reason = models.CharField( 
        max_length=190,
        default='purchace'
        )
    amount = models.DecimalField(
        default=0.00, 
        max_digits=8, 
        decimal_places=2)
    datetime = models.DateTimeField(
        auto_now_add=True
        )

    def __str__(self):
        return "Списание со счета " + self.user.name + " " + datatimes