# Generated by Django 4.0.5 on 2022-06-21 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('AccountId', models.AutoField(primary_key=True, serialize=False)),
                ('AccountKind', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ClientInfo',
            fields=[
                ('clientId', models.AutoField(primary_key=True, serialize=False)),
                ('ClientName', models.CharField(max_length=100)),
                ('ClientSurname', models.CharField(max_length=100)),
                ('ClientEmail', models.CharField(max_length=100)),
                ('ClientNumber', models.CharField(max_length=10)),
                ('ClientIdNumber', models.CharField(max_length=13)),
                ('ClientPassword', models.CharField(max_length=100)),
                ('Account', models.CharField(max_length=100)),
            ],
        ),
    ]
