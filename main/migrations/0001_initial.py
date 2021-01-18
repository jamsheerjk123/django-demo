# Generated by Django 3.1.5 on 2021-01-12 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=60, unique=True)),
                ('price', models.PositiveIntegerField()),
                ('description', models.TextField(null=True)),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]
