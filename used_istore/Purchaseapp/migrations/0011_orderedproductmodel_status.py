# Generated by Django 4.1.3 on 2023-01-05 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commonapp', '0010_productmodel_category'),
        ('Purchaseapp', '0010_remove_orderedproductmodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderedproductmodel',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='commonapp.statusmodel'),
        ),
    ]
