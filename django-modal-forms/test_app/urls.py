from django.conf.urls import include, url
from django.urls import path
from .views import HomeView, TestFormView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^test-form/$', TestFormView.as_view(), name="test-form"),
    path(r'test-form/<path:pk>/', TestFormView.as_view()),
]
