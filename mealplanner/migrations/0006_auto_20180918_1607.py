# Generated by Django 2.1 on 2018-09-18 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealplanner', '0005_auto_20180918_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='on_sale',
            field=models.BooleanField(default=1),
        ),
    ]
