# Generated by Django 4.1.4 on 2023-01-03 11:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("portfolios", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Snapshot",
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
                    "uusid",
                    models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
                ),
                ("slug", models.SlugField(max_length=63, unique=True)),
                ("date", models.DateTimeField()),
                ("deposit", models.FloatField()),
                ("cash", models.FloatField()),
                ("value", models.FloatField()),
                ("annual_gain", models.FloatField()),
                ("annual_yield", models.FloatField()),
                ("annual_dividends", models.FloatField()),
                ("transactions_cost", models.FloatField()),
                ("transactions_counter", models.IntegerField()),
                (
                    "portfolio",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="snapshots",
                        to="portfolios.portfolio",
                    ),
                ),
            ],
        ),
    ]