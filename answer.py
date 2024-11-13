
"""
Questons 1:
========================================================================================================
For an OOP program about a Rectangle, please follow the instructions provided above each function.
"""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # This area function is used to return the area of a rectangle, use the rectangle function that area = width * height.
    # Example: area for a rectangle(3,4) will be 3 * 4 = 12.
    def area(self):
        return 
    
    # This perimeter function is used to return the perimeter of a rectangle.
    # Example: preimeter for a rectangle(3,4) will be (3+4) * 2 = 14.
    def perimeter(self):
        return 
    
    # This diagonal function is used to compute the length of the diagonal of the rectangle using the Pythagorean theorem.
    # Example: diagonal for a rectangle(3,4) will be square(3^2 + 4^2) = 5
    def diagonal(self):
        return 
    

    # This is_square function is used to check if this rectangle is square, if this rectangle is square, return True, otherwise return False.
    # Checks if the rectangle is a square (i.e., if its width and height are equal).
    # Example: is_square for a rectangle(3,4) will be False
    # Example: is_square for a rectangle(4,4) will be True
    def is_square(self):
        return 
    
    #This resize function is used to resize the rectangle. New_width and new_height are the new width and height.
    def resize(self, new_width, new_height):
        self.width = 
        self.height = 
