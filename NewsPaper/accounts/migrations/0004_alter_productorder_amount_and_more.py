# Generated by Django 4.2 on 2023-04-12 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_orders_product_composition_alter_staff_position_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productorder',
            name='amount',
            field=models.IntegerField(db_column='amount', default=1),
        ),
        migrations.RenameField(
            model_name='productorder',
            old_name='amount',
            new_name='_amount',
        ),
        migrations.RenameField(
            model_name='productorder',
            old_name='order_rel',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='productorder',
            old_name='staff_rel',
            new_name='product',
        ),
    ]
