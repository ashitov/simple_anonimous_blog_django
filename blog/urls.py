from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.get_blog, name='get_blog')
]