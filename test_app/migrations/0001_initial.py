# Generated by Django 4.0.8 on 2022-12-12 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('description', models.TextField()),
                ('phone_number', models.PositiveIntegerField()),
                ('is_live', models.BooleanField()),
                ('amount', models.FloatField()),
            ],
        ),
    ]