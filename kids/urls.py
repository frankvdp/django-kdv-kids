from django.conf.urls.defaults import patterns, url
from django.views.generic.list_detail import *
from kids.views import *
# from django.views.decorators.cache import cache_page


urlpatterns = patterns('',
    url(r'^groepen/?$', GroupListView.as_view(), name='GroupListView'),
    url(r'^groepen/groep/(?P<slug>[a-zA-Z0-9-_]+)\.html$', GroupDetailView.as_view(), name='GroupView'),
    url(r'^verzorgers/verzorger/(?P<slug>[a-zA-Z0-9-_]+)\.html$', CaretakerDetailView.as_view(), name='CaretakerView'),

    url(r'^kids/kind/(?P<slug>[a-zA-Z0-9-_]+)\.html$', KidDetailView.as_view(), name='KidView'),
    # Examples:
    # url(r'^([a-zA-Z0-9-_]+)$', (ArticleTypeListView.as_view()),  name='typeView'),
    # url(r'^([a-zA-Z0-9-_]+)/populair.html$', cache_page(60 * 5)(ArticleTypePopularListView.as_view()),  name='typePopularView'),
    # url(r'^tags/([a-zA-Z0-9-_]+).html$', ArticleTagList.as_view(),  name='tagView'),
    # url(r'^([a-zA-Z0-9-_]+)/tags/([a-zA-Z0-9-_]+).html$', TagTypeListView.as_view(),  name='tagView'),
    # url(r'^(.+)/categories/(.+).html$', CategoryTypeListView.as_view(), name='categoryTypeView'),
    # url(r'^categories/([a-zA-Z0-9-_]+).html$', CategoryListView.as_view(), name='categoryView'),
    # url(r'^authors/([a-zA-Z0-9-_]+).html$', AuthorListView.as_view(), name='authorView'),
    # url(r'^(?P<type>[a-zA-Z0-9\-_]+)/(?P<slug>[a-zA-Z0-9-_]+)\.html$', 'articles.views.view', name='articleView'),

)
