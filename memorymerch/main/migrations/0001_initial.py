# Generated by Django 5.0.2 on 2024-02-12 18:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catgname', models.CharField(default='', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Tovar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tovarname', models.CharField(default='', max_length=100)),
                ('tovarprice', models.FloatField()),
                ('shipping', models.TextField(default='', max_length=300)),
                ('tovardescrpt', models.TextField(default='', max_length=500)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tovars_categories', to='main.categories')),
            ],
        ),
    ]
