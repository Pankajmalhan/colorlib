# Generated by Django 2.2.2 on 2019-06-26 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20190626_0249'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.TextField(default='', max_length=1200),
        ),
    ]