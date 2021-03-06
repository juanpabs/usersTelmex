# Generated by Django 3.1.3 on 2020-11-22 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('CompanyId', models.AutoField(primary_key=True, serialize=False)),
                ('CompanyName', models.CharField(max_length=100)),
                ('CompanyType', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('RoleId', models.AutoField(primary_key=True, serialize=False)),
                ('RoleName', models.CharField(max_length=100)),
                ('Salary', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('UserName', models.CharField(max_length=100)),
                ('UserEmail', models.CharField(max_length=100)),
                ('Company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UsersApp.companies')),
            ],
        ),
        migrations.CreateModel(
            name='UserRoles',
            fields=[
                ('UserRoleId', models.AutoField(primary_key=True, serialize=False)),
                ('Role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UsersApp.roles')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UsersApp.users')),
            ],
        ),
    ]
