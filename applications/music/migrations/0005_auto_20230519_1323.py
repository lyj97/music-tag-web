# Generated by Django 2.2.6 on 2023-05-19 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20230519_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='comment',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='description',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='paths',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
