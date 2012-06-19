from django.contrib import admin

from currencies.models import CurrencyItem


__all__ = ['CurrencyItemAdmin', ]


class CurrencyItemAdmin(admin.ModelAdmin):
    """ Docstring """
    list_display = ('cname', 'csymbol', 'crate_base', 'crate_base_inverse',
                    'is_base')
    search_fields = ('cname', 'csymbol',)
    fieldsets = (
        ('Currency Info', {
            'fields': ('cname', 'csymbol', 'crate_base', 'crate_base_inverse',
                       'is_base'),
        }),
    )


admin.site.register(CurrencyItem, CurrencyItemAdmin)