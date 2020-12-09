from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

from .views import (NotFoundView, TestView, index_view, login_view,
                    logout_view, profile_view, signup_view)

urlpatterns = [
    path('', index_view, name="index"),
    path('test', TestView.as_view(), name="test"),
    path('404', NotFoundView.as_view(), name='not_found'),
    path('about',
         TemplateView.as_view(template_name='about.html'),
         name='about'),
    path('sub-forum',
         TemplateView.as_view(template_name='sub-forums.html'),
         name='sub_forums'),
    path('forums',
         TemplateView.as_view(template_name='forums.html'),
         name="forums"),
    path('topics',
         TemplateView.as_view(template_name='topics.html'),
         name="topics"),
    path('topic-replies',
         TemplateView.as_view(template_name='topic-replies.html'),
         name="topic-replies"),
    path('faq', TemplateView.as_view(template_name='faq.html'), name="faq"),
    path('group-forum',
         TemplateView.as_view(template_name='group-forum.html'),
         name="group-forum"),
    path('group-home',
         TemplateView.as_view(template_name='group-home.html'),
         name="group-home"),
    path('group-media',
         TemplateView.as_view(template_name='group-media.html'),
         name="group-media"),
    path('group-members',
         TemplateView.as_view(template_name='group-members.html'),
         name="group-members"),
    path('groups',
         TemplateView.as_view(template_name='groups.html'),
         name="groups"),
    path('login', login_view, name="login"),
    path('signup', signup_view, name="sign_up"),
    path('logout', logout_view, name='logout'),
    path('profile', profile_view, name='profile'),
]

# for static files

urlpatterns += static('img/',
                      document_root=settings.BASE_DIR / 'homepage/static/img')
urlpatterns += static('js/',
                      document_root=settings.BASE_DIR / 'homepage/static/js')
urlpatterns += static('css/',
                      document_root=settings.BASE_DIR / 'homepage/static/css')
urlpatterns += static('fonts/',
                      document_root=settings.BASE_DIR /
                      'homepage/static/fonts')
urlpatterns += static('vendor/',
                      document_root=settings.BASE_DIR /
                      'homepage/static/vendor')
