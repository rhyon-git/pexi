# Generated by Django 5.1.3 on 2024-12-14 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PexiApp', '0002_complanits_model_feedback_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback_model',
            name='type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
