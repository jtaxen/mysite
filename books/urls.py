from django.conf.urls import url

from . import views

app_name = 'books'
urlpatterns = {
    url(r'^$', views.AuthorListView.as_view(), name='author_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.AuthorView.as_view(), name='author'),
    url(r'^(?P<pk>[0-9]+)/(?P<book_id>[0-9]+)/$', views.BookView.as_view(), name='book'),
}
