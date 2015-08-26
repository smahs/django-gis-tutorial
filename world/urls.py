from django.conf.urls import url, include
from django.contrib.gis import admin
from views import GetCountryByLL


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^country', GetCountryByLL.as_view()),
]
