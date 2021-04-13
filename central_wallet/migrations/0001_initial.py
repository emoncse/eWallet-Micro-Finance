# Generated by Django 3.2 on 2021-04-13 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('investor', '0001_initial'),
        ('loan_seeker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CentralWallet',
            fields=[
                ('loan_id', models.AutoField(primary_key=True, serialize=False)),
                ('loan_amount', models.FloatField(default=0.0)),
                ('interest_rate', models.FloatField(default=1.0)),
                ('wallet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan_seeker.loanseekerswallet')),
            ],
            options={
                'db_table': 'Central_Wallet',
            },
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('serial_no', models.IntegerField(primary_key=True, serialize=False)),
                ('user_type', models.CharField(db_column='User', default='', max_length=11)),
                ('transaction_type', models.CharField(default='', max_length=20)),
                ('transaction_amount', models.FloatField(default=0.0)),
                ('date', models.DateTimeField()),
                ('remarks', models.TextField(default='')),
            ],
            options={
                'db_table': 'Transactions',
            },
        ),
        migrations.CreateModel(
            name='LoanLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provided_amount', models.FloatField(default=0.0)),
                ('date_time', models.DateTimeField()),
                ('profit_amount', models.FloatField(default=0.0)),
                ('loan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='central_wallet.centralwallet')),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='investor.investorswallet')),
            ],
            options={
                'db_table': 'Loan_Log',
            },
        ),
    ]
