from django.conf.urls import patterns, include, url
from django.contrib import admin
from forum.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'educ.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', Forum.as_view(), name='forum'),
    url(r'^api-auth/post/$', ForumPostList.as_view(), name='forumpost-list'),
    url(r'^api-auth/post/(?P<pk>\d+)/$', ForumPostDetail.as_view(), name='forumpost-detail'),
    url(r'^api-auth/comment/$', ForumCommentList.as_view(), name='forumcomment-list'),
    url(r'^api-auth/comment/(?P<pk>\d+)/$', ForumCommentDetail.as_view(), name='forumcomment-detail'),
)
