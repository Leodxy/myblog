from django.conf.urls import url,include
from . import views
app_name = 'users'
urlpatterns=[
    url(r'^users/', include('django.contrib.auth.urls')),
    url(r'^register/',views.register,name="register"),
    url(r'^$', views.index, name="index"),


]