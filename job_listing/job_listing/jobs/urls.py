from django.conf.urls import include, url

from . import views


urlpatterns = [
    url(r'^$', views.land, name='landpage'),
    url(r'^newjob/', views.new_job_listing, name='newjob'),
    url(r'^myjobs/', views.myjobs, name='myjobs'),
    url(r'^deletejob/(?P<job_posting_id>\d+)/$', views.deletejob, name='delete')
]
