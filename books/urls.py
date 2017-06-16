from django.conf.urls import url

from . import views

app_name = 'books'
urlpatterns = {
    url(r'^([a-z]+)/$', views.AuthorView.as_view(), name='author'),
    url(r'^([a-z]+)/([a-z]+)/$', views.BookView.as_view(), name='book'),
}
