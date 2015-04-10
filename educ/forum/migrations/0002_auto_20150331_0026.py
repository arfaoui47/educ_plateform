# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='professor',
            field=models.ForeignKey(to='forum.Professor'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='forumcomment',
            name='profile_post',
            field=models.ForeignKey(to='forum.ForumPost'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='forumcomment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='forumpost',
            name='student',
            field=models.ForeignKey(to='forum.Student'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='classroom',
            field=models.ForeignKey(to='forum.Classroom'),
            preserve_default=True,
        ),
    ]
