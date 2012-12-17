from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

import jingo

from course.models import Course, Department, School


def home(request):
    schools = School.objects.all()
    courses = _make_paginator(
        request,
        Course.objects.filter(department__school__id=100).order_by('-gpa'),
        25)

    if request.GET.get('q'):
        school_id = int(request.GET.get('school', 100))
        q = request.GET.get('q').split(',')
        courses = _make_paginator(
            request,
            Course.objects.filter(reduce(_or_query, q, Q()))
                          .filter(department__school__id=school_id)
                          .order_by('-gpa'),
            25)

    return jingo.render(request, 'senioritis/home.html',
                        {'courses': courses, 'q': request.GET.get('q', ''), 'schools': schools})


def _or_query(query, text):
    query |= Q(department__tag=text)

    if len(text.split()) >= 2:
        query |= Q(name__icontains=text)
    if len(text) > 2:
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
