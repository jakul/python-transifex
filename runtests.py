"""
Based on https://github.com/jakul/python-jsonrpc/blob/master/run-tests.py
"""
import unittest
import os
from transifex import tests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # Auto detect the tests to run
        testPath = os.path.split(tests.__file__)[0]
        testModules = []
        for fileName in os.listdir(testPath):
            if fileName[-3:] == '.py' and fileName != '__init__.py':
                testModules.append('transifex.tests.%s' % fileName[:-3])
    else:
        testModules = sys.argv[1:]

    suite = unittest.TestLoader().loadTestsFromNames(testModules)
    unittest.TextTestRunner(verbosity=5).run(suite)
    
