# Generated by Django 4.2.11 on 2024-03-13 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_alter_tovar_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tovar',
            name='author',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tovar',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
