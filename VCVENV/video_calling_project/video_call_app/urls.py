from django.urls import path
from .views import home, video_call

urlpatterns = [
    path('', home, name='home'),
    path('video_call/', video_call, name='video_call'),
]
