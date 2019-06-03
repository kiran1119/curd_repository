# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('product_id', models.IntegerField(unique=True)),
                ('product_name', models.CharField(max_length=100)),
                ('product_cost', models.IntegerField()),
                ('product_color', models.CharField(max_length=20)),
                ('product_class', models.CharField(max_length=20)),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_mobile', models.BigIntegerField()),
                ('customer_email', models.EmailField(max_length=50)),
            ],
        ),
    ]
