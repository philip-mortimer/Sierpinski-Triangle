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


# The amount by which the side length of an equilateral triangle with a
# horizontal base is to be multiplied to get the height of the
# triangle.
SIDE_LEN_TO_HEIGHT_MULTIPLIER = math.sin(math.pi / 3.0)


def get_triangle_height(side_len):
    return side_len * SIDE_LEN_TO_HEIGHT_MULTIPLIER


def get_main_triangle(side_len, margin_width) -> Triangle:
    """
    Return the main (outermost) triangle (an equilateral triangle with
    a horizontal base).
    """
    height = get_triangle_height(side_len)

    lower_left = Point(margin_width, margin_width)
    top = Point(margin_width + side_len / 2.0, margin_width + height)
    lower_right = Point(margin_width + side_len, margin_width)

    return Triangle(lower_left, top, lower_right)


def get_display_dimensions(main_triangle_side_len, margin_width):
    triangle_height = get_triangle_height(main_triangle_side_len)

    padding = 2.0 * margin_width
    display_height = math.ceil(triangle_height) + padding
    display_width = main_triangle_side_len + padding

    return DisplayDimensions(height = display_height, width = display_width)    


def main():
    display_dimensions = get_display_dimensions(SIDE_LEN, MARGIN_WIDTH)
    graphics = Graphics(display_dimensions, COLOURS)

    main_triangle = get_main_triangle(SIDE_LEN, MARGIN_WIDTH)
    initial_level = len(COLOURS) - 1
    sierpinski(main_triangle, initial_level, graphics)

    status = graphics.save(OUTPUT_PATH)
    if not status.ok:
        print(status.err_str)
        return 1
    print('Created {}.'.format(OUTPUT_PATH))
    return 0


if __name__ == '__main__':
    exit_code = main()
    exit(exit_code)