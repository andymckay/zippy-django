from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework.routers import SimpleRouter

from zippy.sellers.views import SellerViewSet


router = SimpleRouter()
router.register('sellers', SellerViewSet)

admin.autodiscover()
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
