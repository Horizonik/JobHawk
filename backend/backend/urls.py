from django.contrib import admin
from django.urls import path
from jobsearch.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ReactView.as_view(), name="xxx")
]
