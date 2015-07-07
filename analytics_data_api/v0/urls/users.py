import re

from django.conf.urls import patterns, url

from analytics_data_api.v0.views import users as views

USER_URLS = [
    ('profile', views.UserProfileView, 'user_profile'),
]

urlpatterns = []

for path, view, name in USER_URLS:
    urlpatterns += patterns('', url(r'^(?P<pk>.+)/' + re.escape(path) + r'/$', view.as_view(), name=name))
