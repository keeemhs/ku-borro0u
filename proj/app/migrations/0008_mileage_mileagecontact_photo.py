# Generated by Django 3.2.13 on 2022-10-27 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mileage',
            fields=[
                ('username', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('email', models.CharField(blank=True, max_length=45, null=True)),
                ('mileage', models.IntegerField(blank=True, null=True)),
                ('state', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'mileage',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MileageContact',
            fields=[
                ('username', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('email', models.CharField(blank=True, max_length=45, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('bank', models.CharField(blank=True, max_length=45, null=True)),
                ('account_number', models.CharField(blank=True, max_length=45, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'mileage_contact',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('images', models.CharField(blank=True, max_length=100, null=True)),
                ('username', models.CharField(blank=True, max_length=45, null=True)),
                ('ident', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'photo',
                'managed': False,
            },
        ),
    ]