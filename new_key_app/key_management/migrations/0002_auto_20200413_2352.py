# Generated by Django 2.2.7 on 2020-04-13 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('key_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
