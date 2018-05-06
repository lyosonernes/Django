from django.conf.urls import include, url

import test_app

urlpatterns = [
    url(r'^', include('test_app.urls')),
]
