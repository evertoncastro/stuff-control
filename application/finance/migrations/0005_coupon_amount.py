# Generated by Django 5.0rc1 on 2023-12-16 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0004_expense_coupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='amount',
            field=models.FloatField(null=True),
        ),
    ]