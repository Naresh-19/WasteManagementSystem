# Generated by Django 4.2.1 on 2023-07-03 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('waste', '0008_category_user_registration_point_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_registration',
            name='pincode',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='waste_pickup',
            name='collector',
            field=models.ForeignKey(default='NULL', on_delete=django.db.models.deletion.CASCADE, to='waste.collector_registration'),
        ),
        migrations.DeleteModel(
            name='collection_his',
        ),
    ]
