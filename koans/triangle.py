#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    # DELETE 'PASS' AND WRITE THIS CODE
    if not (a and b and c):
        raise TriangleError# edges bigger than zero
    _a, _b, _c = sorted([a, b, c])
    if not (_a + _b > _c):
        raise TriangleError# The sum of any two sides should be greater than the third one
    unequal_sides = len(set([_a, _b, _c]))
    if unequal_sides == 1:
        return 'equilateral'
    elif unequal_sides == 2:
        return 'isosceles'
    else:
        return 'scalene'


# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
