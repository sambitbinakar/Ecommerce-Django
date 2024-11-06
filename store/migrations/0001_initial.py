# Generated by Django 5.1.2 on 2024-11-06 02:29

import django.db.models.deletion
import django.utils.timezone
import django_ckeditor_5.fields
import shortuuid.django_fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.FileField(blank=True, null=True, upload_to='image')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Catagories',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('discount', models.IntegerField(default=100)),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('shipping', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('tax', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('service_fee', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('payment_status', models.CharField(choices=[('processing', 'processing'), ('paid', 'paid'), ('failed', 'failed')], default='processing', max_length=100)),
                ('payment_method', models.CharField(blank=True, choices=[('paypal', 'paypal'), ('PayU', 'PayU'), ('Strip', 'Strip'), ('Razorpay', 'Razorpay')], default=None, max_length=100, null=True)),
                ('order_status', models.CharField(choices=[('shipped', 'shipped'), ('cancelled', 'cancelled'), ('processing', 'processing'), ('fulfilled', 'fulfilled'), ('Pending', 'Pending')], default='Pending', max_length=100)),
                ('inital_total', models.DecimalField(decimal_places=2, default=0.0, help_text='The orginal total', max_digits=12)),
                ('saved', models.DecimalField(blank=True, decimal_places=2, default=0.0, help_text='Amount', max_digits=12, null=True)),
                ('order_id', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=6, max_length=25, prefix='')),
                ('payment_id', models.CharField(blank=True, max_length=1000, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('coupon', models.ManyToManyField(blank=True, to='store.coupon')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer', to=settings.AUTH_USER_MODEL)),
                ('vendor', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Order',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.FileField(blank=True, default='product.jpg', null=True, upload_to='images')),
                ('description', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True, verbose_name='Sale Price')),
                ('regular_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True, verbose_name='Regular price')),
                ('stock', models.PositiveIntegerField(blank='published', default=0, null=True)),
                ('shipping', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True, verbose_name='Shipping amount')),
                ('status', models.CharField(choices=[('published', 'published'), ('draft', 'draft'), ('disabled', 'disabled')], default='published', max_length=50)),
                ('features', models.BooleanField(default=False, verbose_name='Marketplace Features')),
                ('sku', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=5, max_length=50, prefix='SKU', unique=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.category')),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Product',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.CharField(choices=[('shipped', 'shipped'), ('cancelled', 'cancelled'), ('processing', 'processing'), ('fulfilled', 'fulfilled'), ('Pending', 'Pending')], default='Pending', max_length=100)),
                ('shipping_service', models.CharField(blank=True, choices=[('UPS', 'UPS'), ('Fedx', 'fedx'), ('DHL', 'DHL')], default=None, max_length=100, null=True)),
                ('tracking_id', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('qty', models.IntegerField(default=0)),
                ('color', models.CharField(blank=True, max_length=100, null=True)),
                ('size', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('sub_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('shipping', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('tax', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('initial_total', models.DecimalField(decimal_places=2, default=0.0, help_text='Grand total of...', max_digits=12)),
                ('saved', models.DecimalField(blank=True, decimal_places=2, default=0.0, help_text='Amount', max_digits=12, null=True)),
                ('applied_coupon', models.BooleanField(default=False)),
                ('item_id', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=6, max_length=25, prefix='')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('coupon', models.ManyToManyField(blank=True, to='store.coupon')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.order')),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vendor_order_item', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(default='gallery.jpg', upload_to='image')),
                ('gallery_id', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=6, max_length=10, prefix='')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True)),
                ('sub_total', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True)),
                ('shipping', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True)),
                ('tax', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True)),
                ('size', models.CharField(blank=True, max_length=100, null=True)),
                ('color', models.CharField(blank=True, max_length=100, null=True)),
                ('cart_id', models.CharField(blank=True, max_length=1000, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(blank=True, null=True)),
                ('reply', models.TextField(blank=True, null=True)),
                ('rating', models.IntegerField(choices=[(3, '★★★☆☆'), (5, '★★★★★'), (1, '★☆☆☆☆'), (2, '★★☆☆☆'), (4, '★★★★☆')], default=None)),
                ('active', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to='store.product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Varient Name')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='VariantItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Item Title')),
                ('content', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Item Content')),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='varient_item', to='store.variant')),
            ],
        ),
    ]