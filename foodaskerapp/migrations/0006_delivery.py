# Generated by Django 5.1.5 on 2025-01-29 05:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodaskerapp', '0005_alter_menuitem_restaurant_orderdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('delivery_status', models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Delivered', 'Delivered')], default='Pending', max_length=50)),
                ('delivery_date', models.DateTimeField(blank=True, null=True)),
                ('OrderDetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Delivery', to='foodaskerapp.orderdetails')),
            ],
        ),
    ]
