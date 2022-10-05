# Generated by Django 4.0.4 on 2022-07-20 23:25

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('members', '0003_member_bedrooms'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalMember',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128, verbose_name='first_name')),
                ('second_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='second_name')),
                ('first_surname', models.CharField(max_length=128, verbose_name='first_surname')),
                ('second_surname', models.CharField(max_length=128, verbose_name='second_surname')),
                ('titular', models.BooleanField(default=False)),
                ('phone_number', models.CharField(blank=True, max_length=128, null=True, verbose_name='phone_number')),
                ('member_number', models.SmallIntegerField(db_index=True, verbose_name='member_number')),
                ('bedrooms', models.SmallIntegerField(default=2, validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(4)])),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Member',
                'verbose_name_plural': 'historical Members',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalDebt',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('type', models.CharField(choices=[('cuota_social', 'Cuota social'), ('gastos_comunes', 'Gastos comunes'), ('fondo_socorro', 'Fondo socorro'), ('atraso_cuota', 'Atraso cuota'), ('falta_asamblea', 'Falta asamblea'), ('falta_obra', 'Falta obra'), ('convenio_social', 'Convenio social'), ('prestamo_inacoop', 'Préstamo inacoop'), ('salon_comunal', 'Salon comunal'), ('salon_otros', 'Salon otros'), ('saldo_anterior', 'Saldo anterior'), ('otros', 'Otros')], max_length=256, verbose_name='type')),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='created_at')),
                ('ammount', models.FloatField(verbose_name='ammount')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('member', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='members.member')),
            ],
            options={
                'verbose_name': 'historical debt',
                'verbose_name_plural': 'historical debts',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]