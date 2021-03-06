from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pokemonGo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'search.views.index', name='index'),
    #url(r'^pokemon$', 'search.views.index', name = 'index'),
    url(r'^random$', 'search.views.random', name = 'random'),
    url(r'^searchGET$', 'search.views.srchget', name = 'search'),
    url(r'^searchPOST$', 'search.views.srchpost', name = 'searchPOST'),
    url(r'^searchLISTJS$', 'search.views.srchlistjs', name = 'searchLISTJS'),
    url(r'^edit/(\d+)', 'search.views.edit', name = 'edit'),
    url(r'^pokemon/(?P<pokemon_id>\d+)/(?P<pokemon_name>[\w\-]+)', 'search.views.desc', name = 'desc'),
    url(r'^pokemon/(?P<pokemon_id>\d+)/', 'search.views.short_url', name = 'desc'),
    url(r'^p/(?P<page_id>\d+)', 'search.views.index2', name = 'pages'),
    url(r'^oddish/$', 'search.views.oddish', name='oddish'),
    url(r'^game$', 'search.views.game', name = 'game'),
    url(r'^fbshare$', 'search.views.fbshare', name = 'fbshare'),
    url(r'^gshare$', 'search.views.gshare', name = 'gshare'),
    url(r'^linkedin$', 'search.views.linkedin', name = 'linkedin'),
    url(r'^tweet$', 'search.views.tweet', name = 'tweet'),
    #un-named grouping
    #url(r'^search/(\d+)', 'search.views.srch2', name = 'search2'),
    #named-grouping
    #url(r'^search/(?P<foo>\d+)', 'search.views.srch2', name = 'search2'),
    url(r'^searchREDIRECT/(?P<search_string>[\*\w\-]+)/$', 'search.views.srchredirect', name = 'searchredirect'),
)
