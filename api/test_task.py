import os
import time
import xmlrunner
import unittest
from celery import shared_task
from api.cases.config import RunConfig

API_DIR = os.path.dirname(os.path.abspath(__file__))
CASE_DIR = os.path.join(API_DIR, "cases")
REPORT_DIR = os.path.join(API_DIR, "reports")


@shared_task
def run_task(tid, data):
    RunConfig.data = data
    suit = unittest.defaultTestLoader.discover(CASE_DIR, "test_case.py")
    name = time.time()
    report_name = "task{tid}_{time}.xml".format(tid=str(tid), time=str(name).split(".")[0])
    report = os.path.join(REPORT_DIR, report_name)
    with open(report, 'wb') as output:
        xmlrunner.XMLTestRunner(output=output).run(suit)



