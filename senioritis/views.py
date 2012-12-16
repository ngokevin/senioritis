from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

import jingo

from course.models import Course, Department, School


def home(request):
    q = None
    courses = _make_paginator(
        request,
        Course.objects.all().order_by('-gpa'),
        25)

    if request.POST and request.POST.get('q'):
        q = request.POST.get('q').split()
        courses = _make_paginator(
            request,
            Course.objects.filter(reduce(_or_query, q, Q()))
                          .order_by('-gpa'),
            25)

    return jingo.render(request, 'senioritis/home.html',
                        {'courses': courses, 'query': q})


def _or_query(query, text):
    query |= Q(department__tag=text)
    if len(text) > 1:
        query |= Q(professor__icontains=text)
    return query


def _make_paginator(request, qs, num):
    paginator = Paginator(qs, num)
    page = request.GET.get('page')
    try:
        return paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        return paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        return paginator.page(paginator.num_pages)
