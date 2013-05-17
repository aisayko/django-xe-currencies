from django.conf.urls import url

from tastypie.resources import ModelResource
from tastypie.utils import trailing_slash

from xe_currencies.models import CurrencyItem

import decimal


def exchange(csymbol_from, csymbol_to, amount):
    """
    Make currency exchange logic
    """
    try:
        amount = decimal.Decimal(amount)
    except decimal.InvalidOperation:
        return None

    if csymbol_from and csymbol_to and amount:
        try:
            from_currency = CurrencyItem.objects.get(csymbol=csymbol_from)
            to_currency = CurrencyItem.objects.get(csymbol=csymbol_to)
        except CurrencyItem.DoesNotExists:
            return None
        else:
            base_amount = amount * from_currency.crate_base_inverse
            amount = base_amount * to_currency.crate_base

            return '%.2f %s' % (amount, csymbol_to)

    return None


class CurrencyItemResource(ModelResource):
    class Meta:
        queryset = CurrencyItem.objects.all()
        allowed_methods = ['get']
        resource_name = 'currencies'

    def override_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/exchange%s$" % \
                (self._meta.resource_name, trailing_slash()),
                 self.wrap_view('get_exchange'), name="api_get_exchange"),
            ]

    def get_exchange(self, request, **kwargs):
        self.method_check(request, allowed=['get'])
        self.is_authenticated(request)
        self.throttle_check(request)

        csymbol_from = request.GET.get('from', '')
        csymbol_to = request.GET.get('to', '')
        amount = request.GET.get('amount', '')
        result = {}
        exchanged = exchange(csymbol_from, csymbol_to, amount)

        if exchanged:
            result = {
                'from': csymbol_from,
                'to': csymbol_to,
                'result': exchanged
            }

        self.log_throttled_access(request)
        return self.create_response(request, result)
