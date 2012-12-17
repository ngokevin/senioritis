import argparse
import os
import re
import string

from pyquery import PyQuery as pq
import requests

os.environ['DJANGO_SETTINGS_MODULE'] = 'senioritis.settings'
from senioritis.course.models import Course, Department, School


def get_courses(school_url):
    """Master function."""
    print 'Fetching departments from %s' % school_url
    get_department_data(school_url)
    for department_url in get_urls(school_url):

        print 'Fetching courses from %s' % department_url
        for course_url in get_urls(department_url):
            print 'Fetching course from %s' % course_url
            get_course_data(course_url)


def get_urls(url):
    """
    Get links of departments pages that list courses OR
    Get links of course pages that contain course data.
    """
    html = requests.get(url).text
    doc = pq(html)
    return ['https://myedu.com' + a.attrib['href'] for a in doc('a.name')]


def get_department_data(school_url):
    """
    Populate department table with department data.
    """
    html = requests.get(school_url).text
    doc = pq(html)

    # Create school if it doesn't exist.
    school_id = int(doc('.head').attr('data-school-id'))
    school_name = doc('.head h1').text().strip()
    school, created = School.objects.get_or_create(school_id=school_id,
                                                   name=school_name)
    if created:
        print 'Added School %s.' % str(school)

    doc('ul.group li').each(
        lambda e : add_department(e.attr('name'), school_id))


def add_department(department, school_id):
    """Helper function for adding Department object."""
    tag, name = string.split(department, maxsplit=1)
    dept, created = Department.objects.get_or_create(school_id=school_id,
                                                     tag=tag, name=name)
    if created:
        print 'Added Department %s.' % str(dept)


def get_course_data(course_url):
    """
    Load content from course_url and store department,
    course title, course name, gpa, and professor into database.
    """
    html = requests.get(course_url).text
    doc = pq(html)

    try:
        name = doc('.head h2').html().strip()
        title = doc('.head h3').html().strip()
    except AttributeError:
        return
    department = Department.objects.get(tag=name.split()[0])

    doc('tbody.list').each(lambda e : add_course(e, department, name, title))


def add_course(course, department, name, title):
    """Helper function for adding Course object."""
    if course.attr('data-gpa'):
        course, created = Course.objects.get_or_create(
            department=department, name=name, title=title,
            gpa=course.attr('data-gpa'), professor=course.attr('data-name'))
        if created:
            print 'Added Course %s.' % str(course)


if __name__ == '__main__':
    # Place the myedu URL for courses-by-department for your desired school.
    get_courses(
        'https://myedu.com/'
        'OSU-Oregon-State-University/school/100/course/by-department/')
