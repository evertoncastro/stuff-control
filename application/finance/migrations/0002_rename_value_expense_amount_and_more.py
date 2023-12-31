# Generated by Django 5.0rc1 on 2023-12-09 22:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models
from django.contrib.auth import get_user_model

User = get_user_model()
try:
    u_id = User.objects.filter().first().pk
except:
    u_id = 1


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='value',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='expense',
            old_name='checked',
            new_name='verified',
        ),
        migrations.AddField(
            model_name='expense',
            name='user',
            field=models.ForeignKey(default=u_id, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
