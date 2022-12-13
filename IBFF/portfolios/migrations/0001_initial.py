# Generated by Django 4.1.4 on 2022-12-12 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Portfolio",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uupid",
                    models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
                ),
                ("slug", models.SlugField(max_length=63, unique=True)),
                ("name", models.CharField(max_length=31)),
                ("deposit", models.FloatField()),
                ("cash", models.FloatField()),
                ("value", models.FloatField()),
                ("annual_gain", models.FloatField()),
                ("annual_yield", models.FloatField()),
                ("annual_dividends", models.FloatField()),
                ("transactions_cost", models.FloatField()),
                ("transactions_counter", models.IntegerField()),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="portfolios",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]