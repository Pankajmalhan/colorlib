# Generated by Django 2.2.2 on 2019-06-26 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=250)),
                ('availibility', models.BooleanField(default=True)),
                ('width', models.IntegerField(help_text='value in mm')),
                ('height', models.IntegerField(help_text='value in mm')),
                ('depth', models.IntegerField(help_text='value in mm')),
                ('weight', models.IntegerField(help_text='value in gm')),
                ('qualityCheck', models.BooleanField(default=True)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.Category')),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]