from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
	# Examples
	# url(r'^blog/', include('blog.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', include('login.urls')),
	url(r'^login/', include('login.urls')),
	url(r'^todo/', include('todo.urls')),
)
