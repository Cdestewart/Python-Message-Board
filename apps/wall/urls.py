from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^post$', views.post),
    url(r'^comment$', views.comment),
    url(r'^delete$', views.deletecomm),
    url(r'^logoff$', views.logout)
]