from django.conf.urls import patterns, include, url
from django.conf import settings
from tastypie.api import Api
from testApi.api import FoodResource, VoteResource, UserResource, AvatarResource

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(FoodResource())
v1_api.register(VoteResource())
v1_api.register(UserResource())
v1_api.register(AvatarResource())


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'authApp.views.home', name='home'),
    # url(r'^authApp/', include('authApp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('allauth.urls')),
    (r'^api/', include(v1_api.urls)),
    (r'^logged-in/$', 'testApi.views.user_creds'),
    (r'^auth/$', 'testApi.views.auth_approved'),
    (r'^avatar/', include('avatar.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    ) + urlpatterns