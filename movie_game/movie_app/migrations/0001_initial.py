# Generated by Django 5.0 on 2023-12-10 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='actor_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('poster_one', models.CharField(max_length=255)),
                ('poster_two', models.CharField(max_length=255)),
                ('poster_three', models.CharField(max_length=255)),
                ('poster_four', models.CharField(max_length=255)),
            ],
        ),
    ]
