# Generated by Django 5.1.2 on 2024-11-06 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name_plural': 'Gallery'},
        ),
        migrations.RenameField(
            model_name='variantitem',
            old_name='variant',
            new_name='varient',
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='category'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.FileField(default='gallery.jpg', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('processing', 'processing'), ('cancelled', 'cancelled'), ('Pending', 'Pending'), ('fulfilled', 'fulfilled'), ('shipped', 'shipped')], default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.CharField(choices=[('processing', 'processing'), ('failed', 'failed'), ('paid', 'paid')], default='processing', max_length=100),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order_status',
            field=models.CharField(choices=[('processing', 'processing'), ('cancelled', 'cancelled'), ('Pending', 'Pending'), ('fulfilled', 'fulfilled'), ('shipped', 'shipped')], default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='shipping_service',
            field=models.CharField(blank=True, choices=[('DHL', 'DHL'), ('Fedx', 'fedx'), ('UPS', 'UPS')], default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('published', 'published'), ('disabled', 'disabled'), ('draft', 'draft')], default='published', max_length=50),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(5, '★★★★★'), (1, '★☆☆☆☆'), (3, '★★★☆☆'), (2, '★★☆☆☆'), (4, '★★★★☆')], default=None),
        ),
    ]
