# Generated by Django 2.1.7 on 2019-03-05 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0005_auto_20190305_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drinkchoice',
            name='select_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='orders',
            name='flavor1',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='orders',
            name='flavor2',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='orders',
            name='flavor3',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='orders',
            name='flavor4',
            field=models.CharField(max_length=20),
        ),
    ]