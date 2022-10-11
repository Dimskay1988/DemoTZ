# Generated by Django 4.1.2 on 2022-10-11 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.IntegerField()),
                ('brand', models.CharField(blank=True, max_length=60, null=True)),
                ('title', models.CharField(blank=True, max_length=350, null=True)),
            ],
        ),
    ]
