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


# The length of each side of the main (outermost) triangle.
SIDE_LEN = 700

# The width of the margin around the main triangle.
MARGIN_WIDTH = 10

# The fill colours of the triangles. There is 1 colour for each
# recursive level, so the number of recursive levels equals the number 
# of colours.
COLOURS = [
    "rgb(150,150,150)",
    "rgb(171,171,171)",
    "rgb(192,192,192)",
    "rgb(213,213,213)",
    "rgb(234,234,234)",
    "rgb(255,255,255)"
]

OUTPUT_PATH = "sierpinski.svg"

