from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView

urlpatterns = {
    path('quakes/', CreateView.as_view(), name='quakes'),
}

urlpatterns = format_suffix_patterns(urlpatterns)
