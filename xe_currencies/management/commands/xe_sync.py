from django.core.management.base import BaseCommand
from django.conf import settings

from xml.dom import minidom
import urllib2


class Command(BaseCommand):
    """
    Synchronize CurrencyItem's with XE rates database
    """
    def handle(self, *args, **kwargs):
        """ Docstr """
        from xe_currencies.models import CurrencyItem

        dom = minidom.parse(urllib2.urlopen(settings.XE_DATAFEED_URL))
        currencies = dom.getElementsByTagName('currency')
        nodename_to_model_field = {
            'csymbol': 'csymbol',
            'cname': 'cname',
            'crate': 'crate_base',
            'cinverse': 'crate_base_inverse'
        }

        if currencies:
            for currency in currencies:
                model_data = {'is_base': False}

                for childnode in currency.childNodes:
                    if childnode.nodeName in nodename_to_model_field:
                        nodevalue = childnode.childNodes[0].nodeValue
                        fld_name = nodename_to_model_field[childnode.nodeName]
                        model_data[fld_name] = nodevalue

                        if (childnode.nodeName == 'csymbol' and
                            nodevalue == 'EUR'):
                            model_data['is_base'] = True

                if model_data:
                    try:
                        obj = CurrencyItem.objects.get(csymbol=model_data['csymbol'])
                    except CurrencyItem.DoesNotExist:
                        obj = CurrencyItem()

                    obj.csymbol = model_data['csymbol']
                    obj.cname = model_data['cname']
                    obj.crate_base = model_data['crate_base']
                    obj.crate_base_inverse = model_data['crate_base_inverse']
                    obj.is_base = model_data['is_base']
                    obj.save()
        else:
            print 'There are some errors occured.'
