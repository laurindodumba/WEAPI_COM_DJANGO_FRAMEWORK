# Generated by Django 5.0.2 on 2024-02-27 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('cor', models.CharField(max_length=100)),
                ('ano', models.IntegerField(max_length=5)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('capacidade', models.IntegerField(max_length=100)),
            ],
        ),
    ]