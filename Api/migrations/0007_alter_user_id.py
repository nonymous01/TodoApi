# Generated by Django 5.0.2 on 2024-03-01 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0006_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]