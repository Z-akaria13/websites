# Generated by Django 4.2 on 2023-05-02 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='charge_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
