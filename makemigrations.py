#!/usr/bin/env python
# makemigrations.py

from django.core.management import call_command

call_command("makemigrations", "user_models")