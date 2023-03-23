from django.contrib import admin
from django.urls import include, path
from jobsearch import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('jobsearch.urls')),
]
