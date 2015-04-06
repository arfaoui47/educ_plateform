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
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('reg_number', models.IntegerField()),
                ('score', models.IntegerField(default=0)),
                ('skills', models.TextField(blank=True)),
                ('interest', models.TextField(blank=True)),
                ('about', models.TextField(blank=True)),
                ('projects', models.TextField(blank=True)),
                ('classroom', models.ForeignKey(related_name='students', to='forum.Classroom')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
        ),
        migrations.AddField(
            model_name='forumpost',
            name='student',
            field=models.ForeignKey(related_name='forum_posts', to='forum.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumcomment',
            name='profile_post',
            field=models.ForeignKey(related_name='forum_post_comments', to='forum.ForumPost'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumcomment',
            name='user',
            field=models.ForeignKey(related_name='forum_user_comments', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='classroom',
            name='professor',
            field=models.ForeignKey(related_name='classrooms', to='forum.Professor'),
            preserve_default=True,
        ),
    ]
