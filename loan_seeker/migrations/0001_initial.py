# Generated by Django 3.2 on 2021-04-10 22:28

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
            name='LoanSeeker',
            fields=[
                ('wallet_no', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('gender', models.CharField(default='', max_length=6)),
                ('dob', models.DateField(default='0000-00-00')),
                ('occupation', models.CharField(default='', max_length=50)),
                ('institution', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(default='', max_length=50)),
                ('nid', models.CharField(default='', max_length=17)),
                ('image', models.ImageField(default='default.png', upload_to='images')),
                ('phone', models.CharField(default='', max_length=11)),
                ('address', models.CharField(default='', max_length=100, null=True)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Loan_seeker',
            },
        ),
        migrations.CreateModel(
            name='LoanSeekersWallet',
            fields=[
                ('wallet_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='loan_seeker.loanseeker')),
                ('Balance', models.FloatField(default=0.0)),
                ('loan_amount', models.FloatField(default=0.0)),
                ('loan_status', models.CharField(choices=[('Pending', 'Pending'), ('Accept', 'Accept'), ('Reject', 'Reject')], default='Pending', max_length=10)),
                ('deadline', models.DateField(default='0000-00-00')),
                ('loans_approved', models.IntegerField(default=0.0)),
            ],
            options={
                'db_table': 'Loan_seekers_Wallet',
            },
        ),
        migrations.CreateModel(
            name='Instalments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instalment_no', models.IntegerField(default=0)),
                ('instalment', models.FloatField(default=0.0)),
                ('payment', models.FloatField(default=0.0)),
                ('payment_due', models.FloatField(default=0.0)),
                ('payment_date', models.DateField(default='0000-00-00')),
                ('status', models.TextField()),
                ('wallet_no', models.ForeignKey(db_column='Loan_seekers_wallet', on_delete=django.db.models.deletion.PROTECT, to='loan_seeker.loanseeker')),
            ],
            options={
                'db_table': 'Instalments',
            },
        ),
    ]
