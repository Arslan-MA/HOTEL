# Generated by Django 4.2.6 on 2023-10-12 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0003_remove_bookapplication_services_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookapplication',
            name='approve_status',
            field=models.BooleanField(default=False),
        ),
    ]