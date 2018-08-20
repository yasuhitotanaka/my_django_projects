from django.conf.urls import url
from django.conf import settings
from django.views.static import serve

from sake import views


urlpatterns = [
    url(r'^$',views.SakeListView.as_view(), name='SakeListView'),
    url(r'(?P<pk>)[\w-]*/$',views.SakeDetailView.as_view(), name='SakeDetailView'),
    url(r'^sake/$',views.SakeCreatelView.as_view(), name='SakeCreatelView'),
    url(r'^type/$', views.SakeTypeCreatelView.as_view(), name='SakeTypeCreatelView'),
    url(r'^maker/$', views.MakerCreateView.as_view(), name='MakerCreateView'),
    url(r'^maker/list/$', views.MakerListView.as_view(), name='MakerListView'),
    url(r'^media/(?P<path>.*)$', serve, dict(document_root=settings.MEDIA_ROOT)),
]