from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken

from profiles import views

routers = DefaultRouter()
routers.register(f'helloviewset', views.HelloViewset, basename='helloviewset')
routers.register(f'user', views.UserProfileViewset)
routers.register(f"feed", views.ProfileFeedViewset)

urlpatterns = [
    path('helloview/', views.HelloAPIView.as_view()),
    path('login/', ObtainAuthToken.as_view()),
    path('', include(routers.urls)),
]
