from django.conf.urls import url

from . import views

#TODO: Go your own way, live your own life

app_name='table'
urlpatterns = [
    url(r'^$', views.TableView.as_view(), name='table'),
]
