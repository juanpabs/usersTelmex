# Generated by Django 3.1.3 on 2020-11-22 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UsersApp', '0002_auto_20201122_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='Company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='UsersApp.companies'),
        ),
    ]
