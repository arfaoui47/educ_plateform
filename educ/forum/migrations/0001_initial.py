# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('class_name', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
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
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ForumComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contents', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('appreciation', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ForumPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contents', models.TextField()),
                ('hashtags', models.TextField()),
                ('statment', models.BooleanField(default=False)),
                ('approval', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
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
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('cin', models.IntegerField()),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
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
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('reg_number', models.IntegerField()),
                ('score', models.IntegerField(default=0)),
                ('skills', models.TextField(blank=True)),
                ('interest', models.TextField(blank=True)),
                ('about', models.TextField(blank=True)),
                ('projects', models.TextField(blank=True)),
                ('classroom', models.ForeignKey(to='forum.Classroom')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
        ),
        migrations.AddField(
            model_name='reclamation',
            name='sender',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profilepost',
            name='student',
            field=models.ForeignKey(to='forum.Student'),
            preserve_default=True,
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
        migrations.AddField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='note',
            name='professor',
            field=models.ForeignKey(to='forum.Professor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='note',
            name='student',
            field=models.ForeignKey(to='forum.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mailbox',
            name='adresser',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumpost',
            name='student',
            field=models.ForeignKey(to='forum.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumcomment',
            name='forumpost',
            field=models.ForeignKey(to='forum.ForumPost'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumcomment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='club',
            name='student',
            field=models.ForeignKey(to='forum.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='classroom',
            name='professor',
            field=models.ForeignKey(to='forum.Professor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calendar',
            name='classroom',
            field=models.ForeignKey(to='forum.Classroom'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calendar',
            name='professor',
            field=models.ForeignKey(to='forum.Professor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calendar',
            name='student',
            field=models.ForeignKey(to='forum.Student'),
            preserve_default=True,
        ),
    ]
