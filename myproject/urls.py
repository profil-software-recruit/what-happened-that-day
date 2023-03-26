from django.urls import path, include
from myproject_api import urls as myproject_urls

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', include(myproject_urls)),
]
