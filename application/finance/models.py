from django.db import models
from application.common.models import BaseModel


class Expense(BaseModel):
    title = models.CharField(max_length=100)
    value = models.FloatField(default=0.0)
    checked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} | {self.value}"
