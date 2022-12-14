# Generated by Django 4.1.1 on 2022-09-11 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
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
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='digicala.categorymodel')),
            ],
        ),
    ]
