"""insight URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from countries.views import CountryViewSet
from categories.views import CategoryViewSet
from search_settings.views import SearchSettingViewSet
# from words_search_settings.views import WordsSearchSettingViewSet

# Serializers define the API representation.


class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'url', 'username', 'email',
              'is_staff', 'first_name', 'last_name']

# ViewSets define the view behavior.


class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'countries', CountryViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'search_settings', SearchSettingViewSet)
# router.register(r'words_search_settings', WordsSearchSettingViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
