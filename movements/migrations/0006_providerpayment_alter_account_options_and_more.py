# Generated by Django 4.0.4 on 2022-09-01 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movements', '0005_account_alter_historicalpayment_ammount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProviderPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='fecha creacion')),
                ('ammount', models.FloatField(verbose_name='monto')),
                ('currency', models.CharField(max_length=128, verbose_name='moneda')),
            ],
        ),
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'cuenta'},
        ),
        migrations.AlterModelOptions(
            name='historicalpayment',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Pago', 'verbose_name_plural': 'historical Pagos'},
        ),
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name': 'Pago'},
        ),
        migrations.AlterField(
            model_name='historicalpayment',
            name='created_at',
            field=models.DateTimeField(blank=True, editable=False, verbose_name='fecha de creacion'),
        ),
        migrations.AlterField(
            model_name='historicalpayment',
            name='deposited_at',
            field=models.DateField(blank=True, null=True, verbose_name='fecha de depósito'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='deposited_at',
            field=models.DateField(blank=True, null=True, verbose_name='fecha de depósito'),
        ),
    ]
