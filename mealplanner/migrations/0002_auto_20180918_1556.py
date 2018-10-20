# Generated by Django 2.1 on 2018-09-18 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mealplanner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_per_unit', models.FloatField()),
                ('amount', models.FloatField(blank=True, null=True)),
                ('notes', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mealplanner.WeekOfDate')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mealplanner.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='unit',
            name='unit',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AddField(
            model_name='purchasehistory',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mealplanner.Store'),
        ),
        migrations.AddField(
            model_name='purchasehistory',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mealplanner.Unit'),
        ),
    ]
