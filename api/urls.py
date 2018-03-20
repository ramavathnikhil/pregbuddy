from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, TopicsView

urlpatterns = [
    # url(r'^bucketlists/$', CreateView.as_view(), name="create"),
    url(r'^topics/$', TopicsView.as_view(), name="create"),

]
