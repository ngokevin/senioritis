from django.db.models import Q

import jingo

from course.models import Course, Department, School


def home(request):
    q = None
    courses = Course.objects.all().order_by('-gpa')[:25]

    if request.POST and request.POST.get('q'):
        q = request.POST.get('q').split()
        courses = (Course.objects.filter(reduce(_or_query, q, Q()))
                   .order_by('-gpa')[:25])

    return jingo.render(request, 'senioritis/home.html',
                        {'courses': courses, 'query': q})


def _or_query(query, text):
    query |= (Q(department__tag=text))
    return query
