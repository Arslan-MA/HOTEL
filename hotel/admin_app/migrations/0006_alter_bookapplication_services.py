# Generated by Django 4.2.6 on 2023-10-12 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0005_alter_bookapplication_approve_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookapplication',
            name='services',
            field=models.ManyToManyField(blank=True, to='admin_app.service'),
        ),
    ]
