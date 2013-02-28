#!/bin/env/python
# -*- coding: UTF-8 -*-

from BaseTest import *

class PyOpenFLUIDTest_UnitsIDs(PyOpenFLUIDTest):

    def mainTest(self):
        """Test of units IDs functions."""
        self.assertEquals(self.loadAllInputDataset(ArgList), 1)

        # test of unitsA
        ListID = self.openfluid.getUnitsIDs("unitsA")
        self.assertTrue(isinstance(ListID, list))

        ListTest = range(1, 10)
        ListTest.remove(4)
        ListID.sort(); ListTest.sort()
        self.assertEquals(ListID, ListTest)

if __name__ == "__main__":
  ArgList = skipArgFromLC()
  unittest.main()