# Generated by Django 2.1.5 on 2020-09-13 13:50

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(storage=django.core.files.storage.FileSystemStorage(location='~/Documents/'), upload_to='netdisc/photo/')),
                ('location', models.CharField(blank=True, default='', help_text='照片拍摄地', max_length=16)),
                ('desc', models.TextField(blank=True, default='', help_text='照片描述')),
            ],
        ),
    ]
