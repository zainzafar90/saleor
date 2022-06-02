# Generated by Django 3.2.13 on 2022-04-27 09:10

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0064_rewrite_customerevent_order_relation"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="address",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=[
                    "company_name",
                    "street_address_1",
                    "street_address_2",
                    "city",
                    "postal_code",
                    "phone",
                ],
                name="warehouse_address_search_gin",
                opclasses=[
                    "gin_trgm_ops",
                    "gin_trgm_ops",
                    "gin_trgm_ops",
                    "gin_trgm_ops",
                    "gin_trgm_ops",
                    "gin_trgm_ops",
                ],
            ),
        ),
    ]
