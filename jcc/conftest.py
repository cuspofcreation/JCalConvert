import os
import sys


def pytest_configure(config):
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "")))
