# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfessorDocs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to=b'uploads/')),
                ('year', models.IntegerField()),
                ('type', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('classroom', models.ForeignKey(to='authentification.Classroom')),
                ('professor', models.ForeignKey(to='authentification.Professor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('classroom', models.ForeignKey(to='authentification.Classroom')),
                ('professor', models.ForeignKey(to='authentification.Professor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
