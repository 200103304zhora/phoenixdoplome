# Generated by Django 5.0.3 on 2024-04-10 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0008_savingsgoal"),
    ]

    operations = [
        migrations.AlterField(
            model_name="savingsgoal",
            name="current_amount",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]