from django.conf import settings 
from django.conf.urls import patterns, url
from post import views


urlpatterns = patterns('',
	url(r'^$',views.index,name='index'),
	url(r'^announcements/',views.announcements,name='announcements'),
	url(r'^competitions/',views.competitions,name='competitions'),
	url(r'^calendar/',views.calendar,name='calendar'),
	url(r'^about-us/',views.aboutus,name="about-us"),
	url(r'^sponsors/',views.sponsors,name='sponsors'),
	url(r'^projects/',views.projects,name='projects'),
	) 


if settings.DEBUG:
	from django.conf.urls.static import static
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

	urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))