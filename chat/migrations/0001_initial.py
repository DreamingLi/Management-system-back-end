# Generated by Django 3.1.1 on 2020-10-03 06:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.CharField(max_length=60)),
                ('sender', models.CharField(max_length=10)),
                ('receiver', models.CharField(max_length=10)),
                ('content', models.CharField(max_length=255)),
                ('read', models.BooleanField()),
                ('create_time', models.DateTimeField(default=datetime.datetime(2020, 10, 3, 19, 5, 4, 72555))),
            ],
            options={
                'db_table': 'chat',
                'managed': True,
            },
        ),
    ]
