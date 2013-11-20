from django.conf.urls import patterns, include, url
from django.conf import settings
from klr import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'klr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'manager.views.loginUser'),
    url(r'^todos_foros/(?P<id_seccion>.*)$', 'manager.views.todos_foros'),
    url(r'^viaje/crearViaje/$', 'manager.views.crear_viaje'),
    url(r'^viaje/todos_viajes/$', 'manager.views.todos_viajes'),
    
)
