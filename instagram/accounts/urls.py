from __future__ import absolute_import

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(
        r'^(?P<username>[-\w]{5,30})/$',
        views.ProfileView.as_view(),
        name='profile'
    ),
]