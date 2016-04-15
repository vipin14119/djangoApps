from django.conf.urls import url
from . import views

app_name='register'
urlpatterns=[
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
    url(r'^new$',views.new,name='new'),
    url(r'^new/thanks$',views.thanks,name='thanks'),
]