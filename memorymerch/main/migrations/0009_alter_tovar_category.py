# Generated by Django 4.2.11 on 2024-03-13 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_tovar_author_alter_tovar_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tovar',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tovars_categories', to='main.categories'),
        ),
    ]