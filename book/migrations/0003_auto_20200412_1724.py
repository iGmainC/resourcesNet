# Generated by Django 3.0.5 on 2020-04-12 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20200412_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='brief',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
    ]