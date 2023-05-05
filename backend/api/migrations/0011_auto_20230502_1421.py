# Generated by Django 3.2.18 on 2023-05-02 08:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0010_alter_order_destination_address'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserAddress',
            new_name='AddressBook',
        ),
        migrations.AlterModelOptions(
            name='addressbook',
            options={'verbose_name': 'User_address', 'verbose_name_plural': 'User addresses'},
        ),
        migrations.AlterModelOptions(
            name='orderbook',
            options={'verbose_name': 'Order_book', 'verbose_name_plural': 'Order books'},
        ),
        migrations.AlterModelOptions(
            name='orderhistory',
            options={'verbose_name': 'Order_history', 'verbose_name_plural': 'Order histories'},
        ),
        migrations.AlterField(
            model_name='order',
            name='destination_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='api.address'),
        ),
    ]