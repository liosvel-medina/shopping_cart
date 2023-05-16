# Generated by Django 4.2 on 2023-05-16 02:08

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('hex_value', colorfield.fields.ColorField(default='#000000', image_field=None, max_length=18, samples=None)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/products')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('initial_stock', models.IntegerField()),
                ('current_stock', models.IntegerField()),
                ('is_deleted', models.BooleanField(default=False)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.brand')),
                ('main_color', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='%(app_label)s_%(class)s', to='api.color')),
                ('secondary_colors', models.ManyToManyField(blank=True, to='api.color')),
            ],
        ),
        migrations.CreateModel(
            name='TShirt',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.product')),
                ('size', models.CharField(choices=[('xxs', 'XXS'), ('xs', 'XS'), ('s', 'S'), ('m', 'M'), ('l', 'L'), ('xl', 'XL'), ('xxl', 'XXL')], max_length=3)),
                ('sizing', models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('u', 'Unisex')], max_length=2)),
                ('has_sleeves', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 't-shirt',
                'verbose_name_plural': 't-shirts',
            },
            bases=('api.product',),
        ),
        migrations.CreateModel(
            name='Composition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.IntegerField(choices=[(1, 'Cotton'), (2, 'Linen'), (3, 'Hemp'), (4, 'Polyester'), (5, 'Nylon'), (6, 'Wool'), (7, 'Silk')])),
                ('percent', models.FloatField()),
                ('tshirt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tshirt')),
            ],
        ),
        migrations.CreateModel(
            name='Cap',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.product')),
                ('logo_color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='caps', to='api.color')),
            ],
            options={
                'verbose_name': 'cap',
                'verbose_name_plural': 'caps',
            },
            bases=('api.product',),
        ),
    ]
