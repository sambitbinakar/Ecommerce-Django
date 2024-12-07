# Generated by Django 5.1.2 on 2024-11-24 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_order_order_status_alter_order_payment_method_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Brand',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Brand Name'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('processing', 'processing'), ('shipped', 'shipped'), ('fulfilled', 'fulfilled'), ('cancelled', 'cancelled'), ('Pending', 'Pending')], default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('Razorpay', 'Razorpay'), ('Strip', 'Strip'), ('PayU', 'PayU'), ('paypal', 'paypal')], default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order_status',
            field=models.CharField(choices=[('processing', 'processing'), ('shipped', 'shipped'), ('fulfilled', 'fulfilled'), ('cancelled', 'cancelled'), ('Pending', 'Pending')], default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='shipping_service',
            field=models.CharField(blank=True, choices=[('Fedx', 'fedx'), ('DHL', 'DHL'), ('UPS', 'UPS')], default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='product.jpg', null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=0, default=0.0, max_digits=12, null=True, verbose_name='Sale Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='regular_price',
            field=models.DecimalField(blank=True, decimal_places=0, default=0.0, max_digits=12, null=True, verbose_name='Regular price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('draft', 'draft'), ('published', 'published'), ('disabled', 'disabled')], default='published', max_length=50),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, '★☆☆☆☆'), (4, '★★★★☆'), (2, '★★☆☆☆'), (5, '★★★★★'), (3, '★★★☆☆')], default=None),
        ),
    ]
