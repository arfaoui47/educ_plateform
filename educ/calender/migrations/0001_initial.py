# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contents', models.TextField()),
                ('datebegin', models.DateTimeField()),
                ('dateend', models.DateTimeField()),
                ('club', models.CharField(max_length=50)),
                ('classroom', models.ForeignKey(to='authentification.Classroom')),
                ('professor', models.ForeignKey(to='authentification.Professor')),
                ('student', models.ForeignKey(to='authentification.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
