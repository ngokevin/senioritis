import jingo

from course.models import Course, Department, School


def home(request):
    if request.POST:
        pass
    else:
        return jingo.render(request, 'senioritis/home.html')
