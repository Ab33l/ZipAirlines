from django.urls import path, include
from rest_framework import routers

from .views import ZipAirlinesView


router = routers.DefaultRouter()

app_name = 'airlines'
urlpatterns = [
    path('', include(router.urls)),
    path('airplanes/', ZipAirlinesView.as_view(), name='airplane')
]
