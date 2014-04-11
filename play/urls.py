from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

from play import views

urlpatterns = patterns('',
    url(r'^login/$', views.login ,name='login'),  
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^home/$', views.home ,name='home'),
    url(r'^sorry/$', views.sorry ,name='sorry'),
    url(r'^create/$', views.create_event ,name='create_event'),
    url(r'^my_events/$', views.my_events ,name='my_events'),
    url(r'^company/$', views.my_company ,name='my_company'),
    url(r'^reward/$', views.reward ,name='reward'),
    url(r'^$', views.index ,name='index'),




    url(r'^api/registration/$', views.api_registration ,name='api_registration'),
    url(r'^api/login/$', views.api_login ,name='api_login'),
    url(r'^api/home/$', views.api_home ,name='api_home'),
    url(r'^api/logout/$', views.api_logout ,name='api_logout'),
    url(r'^api/my_events/$', views.api_my_events ,name='api_my_events'),
    url(r'^api/events/$', views.api_events ,name='api_events'),
    url(r'^api/my_coupons/$', views.api_my_coupons ,name='api_my_coupons'),
    url(r'^api/coupons/$', views.api_coupons ,name='api_coupons'),
    url(r'^api/leaderboard/$', views.api_leaderboard ,name='api_leaderboard'),

)

