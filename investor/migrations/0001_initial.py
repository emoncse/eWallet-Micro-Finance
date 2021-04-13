# Generated by Django 3.2 on 2021-04-13 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('wallet_no', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('gender', models.CharField(default='', max_length=6)),
                ('dob', models.DateField()),
                ('occupation', models.CharField(default='', max_length=50)),
                ('institution', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(default='', max_length=50)),
                ('nid', models.CharField(default='', max_length=17)),
                ('image', models.ImageField(default='default.png', upload_to='images')),
                ('phone', models.CharField(default='', max_length=11)),
                ('address', models.CharField(default='', max_length=100)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Investor',
            },
        ),
        migrations.CreateModel(
            name='InvestorsWallet',
            fields=[
                ('wallet_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='investor.investor')),
                ('balance', models.FloatField(default=0.0)),
                ('fixed_savings', models.FloatField(default=0.0)),
                ('profit', models.FloatField(default=0.0)),
                ('last_deposit', models.FloatField(default=0.0)),
                ('deposit_date', models.DateField()),
                ('loans_approved', models.IntegerField(default=0)),
                ('loan_amount', models.FloatField(default=0.0)),
            ],
            options={
                'db_table': 'Investors_wallet',
            },
        ),
    ]
