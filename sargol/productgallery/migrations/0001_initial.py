# Generated by Django 3.1.6 on 2021-04-25 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('web', '0008_delete_productsimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='product_gallery')),
                ('productt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.products')),
            ],
            options={
                'verbose_name': 'gallery',
                'verbose_name_plural': 'gallerys',
            },
        ),
    ]
