# Generated by Django 3.2.14 on 2023-02-22 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astercrm', '0003_alter_sales_plant_smno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='plant_smno',
            field=models.IntegerField(max_length=15, unique=True),
        ),
    ]
