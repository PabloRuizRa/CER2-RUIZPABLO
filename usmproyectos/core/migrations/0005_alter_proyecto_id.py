# Generated by Django 5.0.4 on 2024-06-03 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_proyecto_profesor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Id'),
        ),
    ]
