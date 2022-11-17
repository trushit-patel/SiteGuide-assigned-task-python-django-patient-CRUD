# Generated by Django 3.2.4 on 2021-07-29 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_id', models.AutoField(db_column='patientid', primary_key=True, serialize=False, unique=True)),
                ('firstname', models.CharField(db_column='firstname', max_length=70)),
                ('lastname', models.CharField(db_column='lastname', max_length=100)),
                ('gender', models.CharField(db_column='gender', max_length=70)),
                ('age', models.IntegerField(db_column='age')),
                ('disease', models.CharField(db_column='disease', max_length=70)),
                ('doctor', models.CharField(db_column='doctor', max_length=70)),
                ('fees', models.FloatField(db_column='fees')),
                ('medicine_date', models.DateField(db_column='medicine_date')),
            ],
        ),
    ]