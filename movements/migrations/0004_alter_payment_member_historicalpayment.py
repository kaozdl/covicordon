# Generated by Django 4.0.4 on 2022-07-20 23:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_historicalmember_historicaldebt'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movements', '0003_payment_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='payments', to='members.member'),
        ),
        migrations.CreateModel(
            name='HistoricalPayment',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('deposited_at', models.DateField(blank=True, null=True)),
                ('verified', models.BooleanField(blank=True, default=False)),
                ('ammount', models.FloatField()),
                ('attachment', models.TextField(max_length=100)),
                ('reference', models.CharField(max_length=128)),
                ('notes', models.TextField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('member', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='members.member')),
            ],
            options={
                'verbose_name': 'historical payment',
                'verbose_name_plural': 'historical payments',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]