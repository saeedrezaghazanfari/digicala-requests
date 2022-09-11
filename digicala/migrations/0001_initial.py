# Generated by Django 4.1.1 on 2022-09-11 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DigicalaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_page', models.TextField()),
                ('image', models.TextField()),
                ('title', models.CharField(max_length=255)),
                ('properties', models.TextField()),
                ('seller', models.CharField(max_length=255)),
                ('guarantee', models.CharField(max_length=255)),
                ('price', models.PositiveBigIntegerField()),
            ],
        ),
    ]