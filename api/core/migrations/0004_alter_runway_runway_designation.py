# Generated by Django 5.0.1 on 2024-02-04 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_runway_runway_designation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runway',
            name='runway_designation',
            field=models.CharField(choices=[('L', 'Left'), ('C', 'Center'), ('R', 'Right'), ('N', 'None')], max_length=1),
        ),
    ]
