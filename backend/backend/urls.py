from django.contrib import admin
from django.urls import include, path

from jobsearch.views import saml_auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('jobsearch.urls')),
    path('saml2/', include('djangosaml2.urls')),
    path('api/saml-auth/', saml_auth),
]
