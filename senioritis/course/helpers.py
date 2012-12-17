import urllib

import jinja2
from jingo import register


@register.function
@jinja2.contextfunction
def page_url(context, page_num):
    """Copy current GET params to page param."""
    get_params = [(k, v) for k, v in context['request'].GET.items()]
    get_params.append(('page', page_num))

    return u'?%s' % urllib.urlencode(get_params)
