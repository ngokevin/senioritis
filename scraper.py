import argparse
import os
import re
import string

import pyquery as pq
import requests

from senioritis.course.models import Course, Department, School


os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'


def get_courses(school_url):
    """Master function."""
    get_department_data(school_url)
    for department_url in get_urls(school_url):
        for course_url in get_urls(department_url):
            get_course_data(course_url)


def get_urls(url):
    """
    Get links of departments pages that list courses OR
    Get links of course pages that contain course data.
    """
    html = requests.get(url).text
    doc = pq(html)
    return [a.attr('href') for a in doc('a.name')]


def get_department_data(school_url):
    """
    Populate department table with department data.
    """
    html = requests.get(school_url).text
    doc = pq(html)

    # Create school if it doesn't exist.
    school_id = int(doc('.head.name').attr('data-school-id'))
    school_name = doc('.head h1').text().strip()
    school, created = School.objects.get_or_create(school_id=school_id,
                                                   name=school_name)

    departments = [ul.attr('data-name') for ul in doc('ul.group')]
    for department in departments:
        tag, name = string.split(department, maxsplit=1)
        Department.objects.get_or_create(school_id=school_id, tag=tag,
                                         name=name)


def get_course_data(course_url):
    """
    Load content from course_url and store department,
    course title, course name, gpa, and professor into database.
    """
    html = requests.get(course_url).text
    doc = pq(html)

    department = Department.objects.get(tag=name.split()[0])
    name = doc('.head h2').html().strip()
    title = doc('.head h3').html().strip()

    courses = doc('tbody.list')
    for course in courses:
        if course.attr('data-gpa'):
            Course.objects.get_or_create(department=department, name=name,
                                         title=title, gpa=course.attr('gpa'),
                                         professor=course.attr('name'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--school', '-u', type=int)
    args = parser.parse_args()

    get_courses(
        'https://myedu.com/'
        'OSU-Oregon-State-University/school/100/course/by-department/')
