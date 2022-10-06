# Generated by Django 4.0.4 on 2022-10-06 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_alter_historicalmember_options_alter_member_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='debt',
            options={'verbose_name': 'Deuda'},
        ),
        migrations.AlterModelOptions(
            name='historicaldebt',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Deuda', 'verbose_name_plural': 'historical Deudas'},
        ),
        migrations.AddField(
            model_name='historicalmember',
            name='apartment_number',
            field=models.SmallIntegerField(default=0, verbose_name='numero de unidad'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='apartment_number',
            field=models.SmallIntegerField(default=1, verbose_name='numero de unidad'),
            preserve_default=False,
        ),
    ]
