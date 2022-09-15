import pytest


def classify_triangle(a, b, c):
    # Determine if the triangle can be classified into isosceles, equaliteral, scalene, and right
    if type(a) == int and type(a) == type(b) == type(c): 
        if a<1 or b<1 or c<1: 
            return "All Params must be greater than zero!"
        elif a+b <= c:  # Uses the Triangle Inequality Theorm, a+b must be GREATER than c
            return "Not a triangle!"
        elif a == b == c:
            return "This is a Equilateral Triangle!"
        elif round(a**2 + b**2) == round(c**2):
            return "This is a Right Triangle!"
        elif a != b and b != c and c != a:
            return "This is a Scalene Triangle!"
        elif a == b or b == c or c == a:
            return "This is a Isosceles Triangle!"
    else:
        return "All Params must be a integer!"


def test_triangle_isosceles():
    assert classify_triangle(4, 4, 6) == "This is a Isosceles Triangle!"


def test_triangle_scalene():
    assert classify_triangle(2, 3, 4) == "This is a Scalene Triangle!"


def test_triangle_equilateral():
    assert classify_triangle(7, 7, 7) == "This is a Equilateral Triangle!"


def test_triangle_right():
    assert classify_triangle(3, 4, 5) == "This is a Right Triangle!"


def test_triangle_verify1():
    assert classify_triangle(1, 3, 6) == "Not a triangle!"

def test_triangle_verify2():
    assert classify_triangle(
        0, 0, 0) == "All Params must be greater than zero!"

def test_triangle_verify3():
    assert classify_triangle("0", 2, "9") == "All Params must be a integer!"

def test_triangle_verify4():
    assert classify_triangle(-1, -1, -3) == "All Params must be greater than zero!"
