from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.glavnaya, name='glavnaya'),
    url(r'^index', views.index, name='index'),
    url(r'^about_federation', views.about_federation, name='about_federation'),
    url(r'^regions', views.regions, name='regions'),
    url(r'^referee', views.referee, name='referee'),
    url(r'^instructor', views.instructor, name='instructor'),
    url(r'^rukovodstvo', views.rukovodstvo, name='rukovodstvo'),
    url(r'^inst_korpus', views.inst_korpus, name='inst_korpus'),
    url(r'^sud_corpus', views.sud_corpus, name='sud_corpus'),
    url(r'^uch_corpus', views.uch_corpus, name='uch_corpus'),
    url(r'^in_federation', views.in_federation, name='in_federation'),
    url(r'^docx', views.docx, name='docx'),




    url(r'^news$', views.news, name='news'),
    url(r'^novosti/(?P<pk>[0-9]+)/$', views.news_detail, name='news_detail'),


    url(r'^turnirs', views.turnirs, name='turnirs'),
    url(r'^turnirs_result', views.turnirs_result, name='turnirs_result'),


    url(r'^articles', views.articles, name='articles'),
    url(r'^spisok_statey/(?P<pk>[0-9]+)/$', views.articles_detail, name='articles_detail'),


    url(r'^contacts', views.contacts, name='contacts'),
]
