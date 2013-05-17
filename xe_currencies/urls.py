from django.conf.urls.defaults import patterns, include
from api.resources import CurrencyItemResource

from tastypie.api import Api


v1_api = Api(api_name='v1')
v1_api.register(CurrencyItemResource())

urlpatterns = patterns('',
    (r'^api/', include(v1_api.urls)),
)