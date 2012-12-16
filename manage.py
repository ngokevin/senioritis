#!/usr/bin/env python
import os
import site
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "senioritis.settings")

    ROOT = os.path.dirname(os.path.abspath(__file__))
    path = lambda *a: os.path.join(ROOT, *a)
    site.addsitedir(path('senioritis'))

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
