# Generated by Django 5.0.2 on 2024-03-26 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_tovar_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='tovar',
            name='tovarimage',
            field=models.ImageField(default=None, upload_to=None),
        ),
    ]
