"""
The following settings should be defined in your global settings

XE_DATAFEED_URL should be set to your registered XE username.
"""

try:
    from django.conf import settings
except ImportError:
    settings = {}


XE_DATAFEED_URL = 'http://www.xe.com/dfs/datafeed2.cgi?xeuser'
