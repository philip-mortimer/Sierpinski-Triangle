"""
    Copyright 2021 Philip Mortimer
    
    This file is part of Philip Mortimer Example Programs.
    Philip Mortimer Example Programs is free software: you can redistribute it 
    and/or modify it under the terms of the GNU General Public License as 
    published by the Free Software Foundation, either version 3 of the License,
    or (at your option) any later version.
    Philip Mortimer Example Programs is distributed in the hope that it will be
    useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with Philip Mortimer Example Programs.  If not, see 
    <https://www.gnu.org/licenses/>.
"""


import math

from geometry import Point, Triangle
from graphics import DisplayDimensions, Graphics
from sierpinski import sierpinski
from params import SIDE_LEN, MARGIN_WIDTH, COLOURS, OUTPUT_PATH


def get_triangle_height(side_len):
    return math.sin(math.pi / 3.0) * side_len


def get_main_triangle_dimensions(side_len, margin_width):
    """
    Return the dimensions of the main (outermost) triangle (an 
    equilateral triangle with a horizontal base).
 
    Parameters:
    side_len -- The length of each side of the triangle.
    margin_width -- The width of the margin around the triangle.

    Return value:
    Length-2 tuple containing:
    -- The main triangle (Triangle class instance).
    -- The height of the main triangle.
    """
    height = get_triangle_height(side_len)

    lower_left = Point(margin_width, margin_width)
    top = Point(margin_width + side_len / 2.0, margin_width + height)
    lower_right = Point(margin_width + side_len, margin_width)
    
    triangle = Triangle(lower_left, top, lower_right)

    return (triangle, height)


def main():
    triangle, triangle_height = get_main_triangle_dimensions(
        SIDE_LEN, MARGIN_WIDTH)

    padding = 2.0 * MARGIN_WIDTH
    display_width = SIDE_LEN + padding
    display_height = math.ceil(triangle_height) + padding
    display_dimensions = DisplayDimensions(
        height = display_height,
        width = display_width
    )    
    graphics = Graphics(display_dimensions, COLOURS)

    initial_level = len(COLOURS) - 1
    sierpinski(triangle, initial_level, graphics)
    
    status = graphics.save(OUTPUT_PATH)
    if not status.ok:
        print(status.err_str)
        return 1
    print("Created {}.".format(OUTPUT_PATH))
    return 0


if __name__ == '__main__':
    exit_code = main()
    exit(exit_code)