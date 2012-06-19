from django.db import models
from django.utils.translation import ugettext_lazy as _


__all__ = ['CurrencyItem', ]


class CurrencyItem(models.Model):
    """
    Represent Currency in local database
    """
    csymbol = models.CharField(max_length=3, unique=True,
                               verbose_name=_('Symbol'))
    cname = models.CharField(max_length=64,
                             verbose_name=_('Name'))
    crate_base = models.DecimalField(max_digits=16, decimal_places=10,
                                     verbose_name=_('Rate to base currency'))
    crate_base_inverse = models.DecimalField(max_digits=16, decimal_places=10,
                                             verbose_name=_('Inversed rate to base currency'))
    is_base = models.BooleanField(default=False, verbose_name=_('Is base'))

    class Meta:
        ordering = ['cname']

    def __unicode__(self):
        return u'%s(%s)' % (self.cname, self.csymbol)