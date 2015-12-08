# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('likes', models.IntegerField(default=0)),
                ('text', models.TextField()),
                ('image_url', models.CharField(max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('tags', models.ManyToManyField(to='tag.Tag')),
            ],
        ),
    ]
