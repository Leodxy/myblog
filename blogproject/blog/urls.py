from django.conf.urls import url
from . import views
app_name = 'blog'
urlpatterns = [
    # url(r'^index/',views.index,name="index"),
    url(r'^index/', views.IndexView.as_view(),name="index"),
    # url(r'^blog/(?P<pk>[0-9]+)/$',views.detail,name="detail"),
    url(r'^blog/(?P<pk>[0-9]+)/$',views.PostDetailView.as_view(),name="detail"),
    url(r'^author_blog/(?P<author>[a-zA-Z]+)',views.AuthorPostList.as_view(),name="author_blog"),
    # url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    # url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
    url(r'^search/$', views.search, name='search'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^full_blog/$', views.Full_blogView.as_view(), name='full_blog'),
    url(r'^about/$', views.about, name='about'),
]