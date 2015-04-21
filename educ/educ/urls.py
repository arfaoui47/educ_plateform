from django.contrib.auth.decorators import user_passes_test
from django.conf.urls import patterns, include, url
from django.contrib import admin
from partage.views import *
from forum.views import *
from authentification.views import *
from calender.views import *
from notification.views import *
from notes.views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'educ.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^accounts/login/$', 'authentification.views.login'),
    url(r'^accounts/auth/$', 'authentification.views.auth_view'),
    url(r'^accounts/logout/$', 'authentification.views.logout'),
    url(r'^accounts/loggedin/$', 'authentification.views.loggedin'),
    url(r'^accounts/invalid/$', 'authentification.views.invalid_login'),


    url(r'^forum/$', Forum.as_view(), name='forum'),
    url(r'^api-auth/user/$', StudentList.as_view(), name='user-list'),
    url(r'^api-auth/student/$', StudentList.as_view(), name='student-list'),
    url(r'^api-auth/professor/$', ProfessorList.as_view(), name='professor-list'),
    url(r'^api-auth/post/$', ForumPostList.as_view(), name='forumpost-list'),
    url(r'^api-auth/post/(?P<pk>\d+)/$', ForumPostDetail.as_view(), name='forumpost-detail'),
    url(r'^api-auth/comment/$', ForumCommentList.as_view(), name='forumcomment-list'),
    url(r'^api-auth/comment/(?P<pk>\d+)/$', ForumCommentDetail.as_view(), name='forumcomment-detail'),
    url(r'^upload/$', Partage.as_view(), name='partage'),
    url(r'^calender/$', Calender.as_view(),name='calender'),
    url(r'^notification/$', Notifications.as_view(),name='notification'),
    url(r'^api-auth/notification/$', NotificationList.as_view(), name='notification-list'),
    url(r'^api-auth/notification/(?P<pk>\d+)/$', NotificationDetail.as_view(), name='notification-detail'),
    url(r'^notes/$', Notes.as_view(),name='notes'),
    url(r'^api-auth/note/$', NotesList.as_view(), name='notes-list'),
    url(r'^api-auth/note/(?P<pk>\d+)/$', NotesDetail.as_view(), name='notes-detail')

)
