# Generated by Django 4.2.7 on 2024-02-27 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vipadmin', '0004_delete_globalmodelregistry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alltypemodel',
            name='text_field',
            field=models.TextField(null=True),
        ),
    ]
