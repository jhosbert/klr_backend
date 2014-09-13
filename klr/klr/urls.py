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

    url(r'^$', 'manager.views.index'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'usuarios.views.loginUser'),
    url(r'^cerrarSesion/$', 'usuarios.views.cerrarSesion'),
    url(r'^todos_foros/(?P<id_seccion>.*)$', 'foros.views.todos_foros'),
    url(r'^viaje/crearViaje/$', 'manager.views.crear_viaje'),
    url(r'^viaje/todos_viajes/$', 'manager.views.todos_viajes'),
    url(r'^viaje/detalles_viaje/(?P<id_viaje>\d+)$', 'manager.views.detalles_viaje'),
    url(r'^todas_secciones/$', 'foros.views.todas_secciones'),
    url(r'^nuevoForo/(?P<id_seccion>.*)$', 'foros.views.nuevoForo'),
    url(r'^detallesForo/(?P<id_foro>.*)$', 'foros.views.detallesForo'),

)
