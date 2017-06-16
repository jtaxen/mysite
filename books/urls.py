from django.conf.urls import url

from . import views

app_name = 'books'
urlpatterns = {
    url(r'^$', views.AuthorListView.as_view(), name='authorlist'),
    url(r'^(?P<pk>)/$', views.AuthorView.as_view(), name='author'),
    url(r'^(?P<pk>)/(<book_id>)/$', views.BookView.as_view(), name='book'),
}
