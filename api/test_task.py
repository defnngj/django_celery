import os
import time
import xmlrunner
import unittest
from celery import shared_task
API_DIR = os.path.dirname(os.path.abspath(__file__))
CASE_DIR = os.path.join(API_DIR, "cases")
REPORT_DIR = os.path.join(API_DIR, "reports")


@shared_task
def run_task():
    suit = unittest.defaultTestLoader.discover(CASE_DIR, "test_case.py")
    name = time.time()
    report = os.path.join(REPORT_DIR, str(name).split(".")[0] + '.xml')
    with open(report, 'wb') as output:
        xmlrunner.XMLTestRunner(output=output).run(suit)



