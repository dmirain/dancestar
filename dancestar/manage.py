#!/usr/bin/env python

from django.core.management import execute_from_command_line

import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dancestar.settings")

def django_main():
    execute_from_command_line(sys.argv)
