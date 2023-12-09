from django.db import models
from application.common.models import BaseModel
from application.authentication.models import User


class Expense(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.FloatField(default=0.0)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} | {self.amount}"
