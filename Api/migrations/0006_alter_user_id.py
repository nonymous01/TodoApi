# Generated by Django 5.0.2 on 2024-03-01 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0005_alter_todo_status_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
