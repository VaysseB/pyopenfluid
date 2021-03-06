#!/bin/env/python
# -*- coding: UTF-8 -*-

from BaseTest import *
import tempfile

class PyOpenFLUIDTest_Simulation(PyOpenFLUIDTest):

    def runTest(self):
        """Test of simulation functions."""

        # creation of a temporary output file and redirecting standard outputs
        FakeOutputFile = tempfile.TemporaryFile(mode="w+b", bufsize=-1)
        sys.stdout = FakeOutputFile
        sys.stderr = FakeOutputFile

        # calling method
        try:
            self.openfluid.printSimulationInfo()
        except Exception as exc:
            sys.__stderr__.write(exc.__name__ + ": " + exc.message)

        self.assertGreater(FakeOutputFile.tell(), 10, "function 'printSimulationInfo' didn't print anything")

        # removing temporary output file
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        FakeOutputFile.close() # destroyed


if __name__ == "__main__":
    unittest.main()
