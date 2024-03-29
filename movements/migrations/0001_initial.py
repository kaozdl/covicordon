# Generated by Django 4.0.4 on 2024-02-22 01:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("members", "__first__"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Account",
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
                ("name", models.CharField(max_length=128, verbose_name="nombre")),
                ("ammount", models.FloatField(verbose_name="saldo")),
                ("currency", models.CharField(max_length=128, verbose_name="moneda")),
            ],
            options={
                "verbose_name": "cuenta",
            },
        ),
        migrations.CreateModel(
            name="ProviderPayment",
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
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="fecha creacion"
                    ),
                ),
                ("ammount", models.FloatField(verbose_name="monto")),
                ("currency", models.CharField(max_length=128, verbose_name="moneda")),
                ("description", models.TextField(verbose_name="descripción")),
                (
                    "provider",
                    models.CharField(max_length=128, verbose_name="proveedor"),
                ),
            ],
            options={
                "verbose_name": "Pago Proveedor",
                "verbose_name_plural": "Pagos a proveedores",
            },
        ),
        migrations.CreateModel(
            name="Payment",
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
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="fecha de creacion"
                    ),
                ),
                (
                    "deposited_at",
                    models.DateField(
                        blank=True, null=True, verbose_name="fecha de depósito"
                    ),
                ),
                (
                    "verified",
                    models.BooleanField(
                        blank=True, default=False, verbose_name="verificado"
                    ),
                ),
                ("ammount", models.FloatField(verbose_name="monto")),
                ("attachment", models.FileField(upload_to="", verbose_name="adjunto")),
                (
                    "reference",
                    models.CharField(max_length=128, verbose_name="num referencia"),
                ),
                (
                    "notes",
                    models.TextField(blank=True, null=True, verbose_name="notas"),
                ),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="payments",
                        to="members.member",
                    ),
                ),
            ],
            options={
                "verbose_name": "Pago",
            },
        ),
        migrations.CreateModel(
            name="HistoricalPayment",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        blank=True, editable=False, verbose_name="fecha de creacion"
                    ),
                ),
                (
                    "deposited_at",
                    models.DateField(
                        blank=True, null=True, verbose_name="fecha de depósito"
                    ),
                ),
                (
                    "verified",
                    models.BooleanField(
                        blank=True, default=False, verbose_name="verificado"
                    ),
                ),
                ("ammount", models.FloatField(verbose_name="monto")),
                (
                    "attachment",
                    models.TextField(max_length=100, verbose_name="adjunto"),
                ),
                (
                    "reference",
                    models.CharField(max_length=128, verbose_name="num referencia"),
                ),
                (
                    "notes",
                    models.TextField(blank=True, null=True, verbose_name="notas"),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "member",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="members.member",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Pago",
                "verbose_name_plural": "historical Pagos",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
