django-xe-currencies
===

**django-xe-currencies** allows you to create your own currency exchange API synced with XE datafeed service.

Quickstart:
===

Install django-xe-currencies:

    $ pip install django-xe-currencies

Add tinymce and xe_currencies to INSTALLED_APPS in settings.py for your project:

    INSTALLED_APPS = (
        ...
        'xe_currencies',
    )
    
Add xe_currencies.urls to urls.py for your project:

    urlpatterns = patterns('',
        ...
        url(r'^currencies/', include('xe_currencies.urls'))
    )

Specify XE_DATAFEED_URL in your settings.py:

    XE_DATAFEED_URL = 'http://www.xe.com/dfs/datafeed2.cgi?xeuser'

To make a synchronization with XE datafeed run:

    python manage.py xe_sync


Access api at the next url:

    http://yourdomain.com/currencies/api/v1/currencies/exchange/?from=EUR&to=USD&amount=100&format=json

This example will return exchange data in JSON format:

    {"from": "EUR", "to": "USD", "result": "143.45 USD"}

To retrieve currencies list use:

    http://example.com/currencies/api/v1/currencies/?format=json
    
Using exchange in your code:
    
    from xe_currencies.api.resources import exchange
    
    exchange('EUR', 'USD', 100)
