# Generated by Django 3.1.6 on 2021-02-17 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_articles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='status',
            field=models.CharField(choices=[('d', 'پیش ساز'), ('p', 'منتشر شده')], max_length=1, verbose_name='وضعیت'),
        ),
    ]
