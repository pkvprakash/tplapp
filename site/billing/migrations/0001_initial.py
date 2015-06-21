# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bill_name', models.CharField(max_length=100)),
                ('bill_star', models.CharField(max_length=60)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BillMeta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('billing_date', models.DateTimeField(auto_now=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='God',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('god_name', models.CharField(max_length=100)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('offer_name', models.CharField(max_length=40)),
                ('offer_price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('offer_god', models.ForeignKey(to='billing.God')),
            ],
        ),
        migrations.CreateModel(
            name='OfferType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_name', models.CharField(max_length=20)),
                ('type_short', models.CharField(max_length=3)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='billmeta',
            name='billing_type',
            field=models.ForeignKey(to='billing.OfferType'),
        ),
        migrations.AddField(
            model_name='bill',
            name='bill_meta_id',
            field=models.ForeignKey(to='billing.BillMeta'),
        ),
        migrations.AddField(
            model_name='bill',
            name='bill_offer',
            field=models.ForeignKey(to='billing.Offer'),
        ),
    ]
