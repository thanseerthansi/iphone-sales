# Generated by Django 4.1.3 on 2022-12-21 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commonapp', '0006_categorymodel_modelnamemodel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='model_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='commonapp.modelnamemodel'),
        ),
    ]
