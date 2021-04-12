# Generated by Django 3.2 on 2021-04-11 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loan_seeker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_amount', models.FloatField(default=0.0)),
                ('loan_approval', models.BooleanField(default=False)),
                ('date', models.DateField(default='0000-00-00')),
                ('wallet_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan_seeker.loanseekerswallet')),
            ],
            options={
                'db_table': 'Loan_Application',
            },
        ),
    ]