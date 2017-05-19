from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from blog import views

urlpatterns = [
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.category_list, name='category_list'),
    url(r'^post', views.post_list, name='post_list'),
    url(r'^place', views.place_list, name='place_list'),
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<pk>\d+)/place_detail$', views.place_detail, name='place_detail'),
    url(r'^new/$', views.post_new, name='post_new'),
    url(r'^new/place$', views.place_new, name='place_new'),
    url(r'^(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),
    url(r'^(?P<pk>\d+)/comment/$', views.add_comment, name='add_comment'),
    url(r'^(?P<pk>\d+)/edit_place/$', views.place_edit, name='place_edit'),
    url(r'^(?P<pk>\d+)/add_recommended/$', views.add_recommended, name='add_recommended'),
    url(r'^(?P<pk>\d+)/delete_recommended/$', views.recommended_delete, name='recommended_delete'),
    url(r'^restaurante', views.restaurante_list, name='restaurante_list'),
    url(r'^(?P<pk>\d+)/detail', views.restaurante_detail, name='restaurante_detail'),
    url(r'^hostel_list', views.hostel_list, name='hostel_list'),
    url(r'^(?P<pk>\d+)/detail', views.hostel_detail, name='hostel_detail'),
    url(r'^museum_list', views.museum_list, name='museum_list'),
    url(r'^(?P<pk>\d+)/detail', views.museum_detail, name='museum_detail'),
    url(r'^(?P<pk>\d+)/place_delete/$', views.place_delete, name='place_delete'),
    url(r'^language', views.words_list, name='words_list'),
    url(r'^polish', views.words_list2, name='dictionary_polish'),
    url(r'^word_new', views.word_new, name='word_new'),
    url(r'^(?P<pk>\d+)/word_edit/$', views.word_edit, name='word_edit'),
    url(r'^(?P<pk>\d+)/word_translation$', views.word_translation, name='word_translation'),
    url(r'^(?P<pk>\d+)/word_delete/$', views.word_delete, name='word_delete'),
    url(r'^author', views.author, name='author'),
    url(r'^add_author', views.add_author, name='add_author'),
]
