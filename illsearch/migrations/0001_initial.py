# Generated by Django 2.1.7 on 2019-05-04 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('num', models.IntegerField(primary_key=True, serialize=False)),
                ('word1', models.CharField(blank=True, default='', max_length=7)),
                ('word2', models.CharField(blank=True, default='', max_length=7)),
                ('word3', models.CharField(blank=True, default='', max_length=7)),
            ],
            options={
                'db_table': 'complain',
            },
        ),
        migrations.CreateModel(
            name='Diagnose',
            fields=[
                ('num', models.IntegerField(primary_key=True, serialize=False)),
                ('ill1', models.CharField(blank=True, default='', max_length=10)),
                ('ill2', models.CharField(blank=True, default='', max_length=10)),
                ('ill3', models.CharField(blank=True, default='', max_length=10)),
                ('ill4', models.CharField(blank=True, default='', max_length=10)),
                ('ill5', models.CharField(blank=True, default='', max_length=10)),
            ],
            options={
                'db_table': 'diagnose',
            },
        ),
        migrations.CreateModel(
            name='Dispose',
            fields=[
                ('num', models.IntegerField(primary_key=True, serialize=False)),
                ('med1', models.CharField(blank=True, default='', max_length=30)),
                ('med2', models.CharField(blank=True, default='', max_length=30)),
                ('med3', models.CharField(blank=True, default='', max_length=30)),
                ('med4', models.CharField(blank=True, default='', max_length=30)),
                ('med5', models.CharField(blank=True, default='', max_length=30)),
                ('med6', models.CharField(blank=True, default='', max_length=30)),
            ],
            options={
                'db_table': 'dispose',
            },
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('num', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=2)),
                ('age', models.CharField(max_length=3)),
                ('section', models.CharField(max_length=5)),
                ('time', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'info',
            },
        ),
    ]