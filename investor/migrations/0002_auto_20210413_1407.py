# Generated by Django 3.2 on 2021-04-13 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investor',
            name='dob',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='investorswallet',
            name='deposit_date',
            field=models.DateField(),
        ),
    ]
