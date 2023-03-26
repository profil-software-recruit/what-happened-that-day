from django.urls import path
from .views import (
    DateListApiView,
    DateDetailApiView,
    PopularListApiView
)

urlpatterns = [
    path('dates/', DateListApiView.as_view()),
    path('dates/<int:date_id>/', DateDetailApiView.as_view()),
    path('popular/', PopularListApiView.as_view()),
]
