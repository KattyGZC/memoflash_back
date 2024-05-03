from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from memo_cards.views import IndexAPIView

urlpatterns = [
    path('', IndexAPIView.as_view(), name='index'),
]

urlpatterns = format_suffix_patterns(urlpatterns)