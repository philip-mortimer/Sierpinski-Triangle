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


from geometry import Point, Triangle
from graphics import Graphics


def get_mid_val(val1, val2):
    return (val1 + val2) / 2.0


def get_mid_point(point1: Point, point2: Point):
    return Point(
        get_mid_val(point1.x, point2.x),
        get_mid_val(point1.y, point2.y)
    )


def get_sub_triangles(triangle: Triangle):
    """
    Return the sub-triangles (central triangle and 3 corner triangles)
    resulting from connecting the mid-points of triangle's sides.

    Parameters:
    triangle -- The triangle to be split into sub-triangles.

    Return value:
    Length-2 tuple containing:
    -- The central triangle (Triangle class instance).
    -- The 3 corner triangles (length-3 tuple containing Triangle class
      instances).
    """
    central_triangle = Triangle(
        get_mid_point(triangle[0], triangle[1]),
        get_mid_point(triangle[1], triangle[2]),
        get_mid_point(triangle[2], triangle[0])
    )    

    corner_triangles = (
        Triangle(triangle[0], central_triangle[0], central_triangle[2]),
        Triangle(triangle[1], central_triangle[1], central_triangle[0]),
        Triangle(triangle[2], central_triangle[2], central_triangle[1])
    )
    return (central_triangle, corner_triangles)



def sierpinski(triangle: Triangle, level, graphics: Graphics):
    """
    Draw the Sierpinski triangle.
    """    
    assert (level >= 0), "level must be >= 0"
    if level == 0:
        graphics.draw_polygon(triangle, level)
    else:
        central_triangle, corner_triangles = get_sub_triangles(triangle)
        graphics.draw_polygon(central_triangle, level)
        for corner_triangle in corner_triangles:
            sierpinski(corner_triangle, level - 1, graphics)

