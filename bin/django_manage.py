#!/usr/bin/env python
import os
import sys

os.sys.path.insert(0,os.getcwd())

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pydash.django_settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
