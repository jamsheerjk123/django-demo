# Generated by Django 3.1.5 on 2021-01-14 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210112_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
