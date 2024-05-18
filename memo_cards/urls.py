from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.decorators.csrf import csrf_exempt
from memo_cards.views import IndexAPIView, ListCardView

urlpatterns = [
    path('', IndexAPIView.as_view(), name='index'),
    path('topic/<int:pk>/', ListCardView.as_view(), name='list-items' )
]

urlpatterns = format_suffix_patterns(urlpatterns)