# Generated by Django 2.2 on 2022-02-22 14:54

from django.db import migrations, models
import places.utils.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_auto_20220222_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='invoice_id',
            field=models.CharField(blank=True, default=places.utils.helpers.generate_invoice_id, max_length=12, unique=True),
        ),
    ]
