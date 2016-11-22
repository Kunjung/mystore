from django.conf.urls import url
from store import views

urlpatterns = [
    
    url(r'^$', views.index, name='index'),
    url(r'^product/(?P<id>[0-9]+)$', views.product, name='product'),
    url(r'^search', views.search, name='search'),
    url(r'^contact', views.contact, name='contact')
]