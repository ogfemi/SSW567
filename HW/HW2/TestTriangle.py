# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Scalene','5,3,4 is a Scalene triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testInput(self): 
        self.assertEqual(classifyTriangle(2,4,6), "NotATriangle")
    
    def testInput2(self): 
        self.assertEqual(classifyTriangle(500,1,5), "InvalidInput")

    def testInput3(self): 
        self.assertEqual(classifyTriangle("0",1,2), "InvalidInput")

    def testInput4(self): 
        self.assertEqual(classifyTriangle(2,1,2), "Isoceles")

    def testInput5(self): 
        self.assertEqual(classifyTriangle(4,4,6) , "Isoceles")
    
    def testInput6(self): 
        self.assertEqual(classifyTriangle(2,3,4) , "Scalene")
    


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

