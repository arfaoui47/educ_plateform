# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0002_auto_20150331_0026'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdministratorDocs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('file', models.CharField(max_length=50)),
                ('target', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contents', models.TextField()),
                ('datebegin', models.DateTimeField()),
                ('dateend', models.DateTimeField()),
                ('club', models.CharField(max_length=50)),
                ('classroom', models.ForeignKey(to='forum.Classroom')),
                ('professor', models.ForeignKey(to='forum.Professor')),
                ('student', models.ForeignKey(to='forum.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('student', models.ForeignKey(to='forum.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MailBox',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contents', models.TextField()),
                ('sender', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('adresser', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note', models.IntegerField()),
                ('subject', models.CharField(max_length=50)),
                ('statement', models.CharField(max_length=50)),
                ('professor', models.ForeignKey(to='forum.Professor')),
                ('student', models.ForeignKey(to='forum.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contents', models.TextField()),
                ('link', models.CharField(max_length=50)),
                ('statement', models.BooleanField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProfessorDocs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('file', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('type', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('professor', models.ForeignKey(to='forum.Professor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProfileComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contents', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProfilePost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contents', models.TextField()),
                ('hashtags', models.TextField()),
                ('statment', models.CharField(default=b'public', max_length=50)),
                ('approval', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(to='forum.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reclamation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contents', models.TextField()),
                ('subject', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('sender', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='profilecomment',
            name='profilepost',
            field=models.ForeignKey(to='forum.ProfilePost'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profilecomment',
            name='student',
            field=models.ForeignKey(to='forum.Student'),
            preserve_default=True,
        ),
        migrations.RenameField(
            model_name='forumcomment',
            old_name='profile_post',
            new_name='forumpost',
        ),
    ]
