import argparse
import os

import pyquery as pq
import requests

from senioritis.course.models import Course, Department


os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'


def get_courses(university_url, university_id):
    """Master function."""
    department_urls = get_department_urls(university_url)


def get_department_urls(university_url):
    """Get links of departments pages that list courses."""
    html = requests.get(university_url).text
    doc = pq(html)
    return doc('a.name')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--university', '-u', type=int)
    args = parser.parse_args()

    get_courses(
        'https://myedu.com/'
        'OSU-Oregon-State-University/school/100/course/by-department/',
        100)
