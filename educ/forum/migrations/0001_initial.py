# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentification', '0001_initial'),
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
            name='Club',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('student', models.ForeignKey(to='authentification.Student')),
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
                ('student', models.ForeignKey(to='authentification.Student')),
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
                ('student', models.ForeignKey(to='authentification.Student')),
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
            field=models.ForeignKey(to='authentification.Student'),
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
    ]
