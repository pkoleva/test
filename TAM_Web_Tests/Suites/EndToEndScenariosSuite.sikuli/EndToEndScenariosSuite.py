import org.sikuli.basics.SikuliXforJython
from sikuli import *
import unittest
import sys
import os

importPath = "C:\\Work\\TAM\\QA\\Tests\\TAM_Web_Tests"
if not importPath in sys.path: sys.path.append(importPath)


import Tests
from Tests import *
from Tests import EndToEndScenarios

from HTMLTestRunner import HTMLTestRunner
  
if Env.isLockOn(Key.NUM_LOCK):
    type(Key.NUM_LOCK)


suite=unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Tests.EndToEndScenarios.EndToEndScenarios))
outfile = open("C:\\Results\\ResultsWebTests.html", "w")
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='All tests', description='All tests' )
runner.run(suite)
