# Generated by Django 3.1.6 on 2021-02-17 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_products_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان مقاله')),
                ('description', models.TextField(verbose_name='متن مقاله')),
                ('status', models.BooleanField(default=True, verbose_name='آیا نمایش داده شود')),
                ('category', models.ManyToManyField(to='web.Category', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'مقاله',
                'verbose_name_plural': 'مقالات',
            },
        ),
    ]
