from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^translate/(?P<text>.*)/$', views.translate, name='translate'),
    ]
