"""
The primary goal of this file is to demonstrate a simple python program to classify triangles
"""


def parameter_check(side_a, side_b, side_c):
    '''verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
        # require that the input values be >= 0 and <= 200

    '''
    if not (isinstance(side_a, int) and isinstance(side_b, int) and isinstance(side_c, int)):
        return False

    if not (0 <= side_a <= 200 and 0 <= side_b <= 200 and 0 <= side_c <= 200):
        return False
    return True


def classify_triangle(side_a, side_b, side_c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of
    you test cases.

    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'

      BEWARE: there may be a bug or two in this code
    """

    if not parameter_check(side_a, side_b, side_c):
        return 'InvalidInput'
        # This information was not in the requirements spec but
        # is important for correctness
        # the sum of any two sides must be strictly less than the third side
        # of the specified shape is not a triangle
    if side_a+side_b <= side_c:
        return 'NotATriangle'

    # now we know that we have a valid triangle
    if side_a == side_b and side_b == side_c:
        return 'Equilateral'
    if ((side_a * side_a) + (side_b * side_b)) == (side_c * side_c):
        return 'Right'
    if (side_a != side_b) and (side_b != side_c) and (side_a != side_c):
        return 'Scalene'
    return 'Isoceles'
