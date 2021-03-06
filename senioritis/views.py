import re

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

import jingo

from course.helpers import clean_sort_param
from course.models import Course, Department, School


def home(request):
    schools = School.objects.all()
    school_id = int(request.GET.get('school', 100))
    courses = _make_paginator(
        request,
        Course.objects.filter(department__school__id=school_id).order_by('-gpa'),
        25)

    if request.GET.get('q'):
        q = request.GET.get('q').split(',')
        courses = _make_paginator(
            request,
            _do_sort(request, Course.objects.filter(reduce(_or_query, q, Q()))
                     .filter(department__school__id=school_id)),
            25)

    return jingo.render(request, 'senioritis/home.html',
                        {'courses': courses, 'q': request.GET.get('q', ''),
                         'schools': schools, 'school_id': school_id})


def _or_query(query, text):
    """Search filtering."""
    text = text.strip()
    query |= Q(department__tag=text)

    if re.match('\w+\d+', text):
        query |= Q(name__icontains=re.sub('([a-zA-Z]+)(\d+)', r'\1 \2', text))
    if len(text.split()) == 2:
        # e.g. MTH 202
        query |= Q(name__icontains=text)
    if len(text) > 4:
        # e.g. Human Evolution
        query |= Q(title__icontains=text)
    if len(text) > 2:
        # e.g. Johnson
        query |= Q(professor__icontains=text)
    return query


def _do_sort(request, qs):
    """Returns an order_by string based on request GET parameters"""
    sort, order = clean_sort_param(request)

    if order == 'asc':
        order_by = sort
    else:
        order_by = '-%s' % sort

    return qs.order_by(order_by)


def _make_paginator(request, qs, num):
    paginator = Paginator(qs, num)
    page = request.GET.get('page', 1)
    try:
        return paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        return paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        return paginator.page(paginator.num_pages)
