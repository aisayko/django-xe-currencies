Welcome to django-currencies-api.

This module allows you to create your own currency exchange API synced with XE datafeed service.

INSTALLATION:

1) Add 'currencies' to INSTALLED_APPS

2) Add url(r'^currencies/', include('currencies.urls')) to your root urls config

3) If you have XE account specify XE_DATAFEED_URL in your settings.py

    a) XE_DATAFEED_URL = 'http://www.xe.com/dfs/datafeed2.cgi?xeuser'

    b) run python manage.py xe_sync


To install requirements see requirements.txt

USAGE:

After you install application you can access api at the next url:

    http://example.com/currencies/api/v1/currencies/exchange/?from=EUR&to=USD&amount=100&format=json

This example will return exchange data in JSON format:

    {"from": "EUR", "result": "143.45 USD", "to": "USD"}

To retrieve currencies list use next url:

    http://example.com/currencies/api/v1/currencies/?format=json