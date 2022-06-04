"""Setup file to run tests"""
import os
import sys

import dotenv
import django
from django.conf import settings
from django.test.utils import get_runner


def run_tests():
    dotenv.load_dotenv()
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.test_settings'
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(['tests'])
    sys.exit(bool(failures))


if __name__ == '__main__':
    run_tests()