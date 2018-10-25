from django.conf.urls import url, include
from django.views.generic import RedirectView
urlpatterns = [
    
    url(r'login/', include('apps.first_app.urls')),
    url(r'wall/', include('apps.wall.urls')),
    url(r'$',RedirectView.as_view(url='login/'))
]