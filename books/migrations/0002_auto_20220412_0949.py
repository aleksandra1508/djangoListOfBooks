# Generated by Django 3.2.5 on 2022-04-12 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='available',
        ),
        migrations.AlterField(
            model_name='book',
            name='number_of_pages',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
