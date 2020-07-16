#!/usr/bin/python
import os

run_tests_cmd = 'python -m unittest discover -v api_tests'
os.system(run_tests_cmd)
