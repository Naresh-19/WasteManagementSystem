# Generated by Django 4.2.1 on 2023-07-03 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('waste', '0009_user_registration_pincode_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField(null=True)),
                ('point', models.IntegerField(null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waste.category')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waste.waste_pickup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='collection_his',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField(null=True)),
                ('point', models.IntegerField(null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waste.category')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waste.waste_pickup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]