# Generated by Django 4.2.1 on 2023-07-22 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waste', '0019_remove_purchase_name_purchase_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='status',
            field=models.CharField(default='Ordered', max_length=20, null=True),
        ),
    ]
