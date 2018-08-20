from django.conf.urls import url
from django.conf import settings
from django.views.static import serve

from sns_majhong import views

app_name = 'sns_majhong'

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^login/$',views.Login.as_view(),name='login'),
    url(r'^logout/$',views.Logout.as_view(),name='logout'),
    url('user_create/',views.UserCreate.as_view(),name='user_create'),
    url('user_create/done', views.UserCreateDone.as_view(), name='user_create_done'),
    url('user_create/complete/<token>/', views.UserCreateComplete.as_view(), name='user_create_complete'),
    url(r'^profile/(?P<pk>\d+)/$', views.UserProfileUpdateView.as_view(), name='user_profile'),
]