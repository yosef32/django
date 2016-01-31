from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from projects import views
urlpatterns = [
    url(r'^projects/$', views.project_list),
    url(r'^projects/(?P<pk>[0-9]+)/$', views.project_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)