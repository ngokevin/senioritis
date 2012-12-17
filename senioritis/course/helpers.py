import urllib

import jinja2
from jingo import register


@register.function
@jinja2.contextfunction
def page_url(context, page_num):
    """Copy current GET params to page param."""
    get_params = [(k, v) for k, v in
                  context['request'].GET.items() if k != 'page']
    get_params.append(('page', page_num))

    return u'?%s' % urllib.urlencode(get_params)


def create_sort_link(pretty_name, sort_field, get_params, sort, order):
    """Generate table header sort links.

    pretty_name -- name displayed on table header
    sort_field -- name of the sort_type GET parameter for the column
    get_params -- additional get_params to include in the sort_link
    sort -- the current sort type
    order -- the current sort order
    """
    get_params.append(('sort', sort_field))

    if sort == sort_field and order == 'asc':
        # Have link reverse sort order to desc if already sorting by desc.
        get_params.append(('order', 'desc'))
    else:
        # Default to ascending.
        get_params.append(('order', 'asc'))

    # Show little sorting sprite if sorting by this field.
    url_class = ''
    if sort == sort_field:
        url_class = ' class="sort-icon ed-sprite-sort-%s"' % order

    return u'<a href="?%s"%s>%s</a>' % (urllib.urlencode(get_params),
                                        url_class, pretty_name)


def clean_sort_param(request):
    """
    Handles empty and invalid values for sort and sort order
    'created' by ascending is the default ordering.
    """
    sort = request.GET.get('sort', 'gpa')
    order = request.GET.get('order', 'desc')

    if sort not in ('name', 'title', 'professor', 'gpa'):
        sort = 'gpa'
    if order not in ('desc', 'asc'):
        order = 'desc'
    return sort, order


@register.function
@jinja2.contextfunction
def sort_link(context, pretty_name, sort_field):
    """Get table header sort links.

    pretty_name -- name displayed on table header
    sort_field -- name of get parameter, referenced to in views
    """
    request = context['request']
    sort, order = clean_sort_param(request)

    # Copy search/filter GET parameters.
    get_params = [(k, v) for k, v in request.GET.items()
                  if k not in ('sort', 'order')]

    return create_sort_link(pretty_name, sort_field, get_params,
                            sort, order)
