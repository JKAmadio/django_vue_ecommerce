# Generated by Django 3.2.6 on 2021-10-06 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]