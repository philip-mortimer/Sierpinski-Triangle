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


from geometry import Point
from Status import Status


MAX_POLYGONS = 50000

TOO_MANY_POLYGONS_ERR = "Number of polygons exceeds maximum ({:g})".format(
    MAX_POLYGONS)

XML_INFO = '<?xml version="1.0"?>'
SVG_INFO = 'xmlns="http://www.w3.org/2000/svg" version="1.1"'


class DisplayDimensions:
    def __init__(self, height, width):
        self._height = height
        self._width = width

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    
def create_point_string(point: Point, display_height):
    x = round(point.get_x())
    y = display_height - round(point.get_y())
    return '{:g},{:g}'.format(x, y)


def create_points_string(points, display_height):
    point_strings = [
        create_point_string(point, display_height) for point in points
    ]
    return ' '.join(point_strings)


def create_polygon_command(points, colour, display_height):
    points_string = create_points_string(points, display_height)
    command = '   <polygon points="{}" style="fill:{}"/>\n'.format(
        points_string, colour)
    return command


def create_svg_header(display_dimensions: DisplayDimensions):
    height_width = 'height="{:g}" width="{:g}"'.format(
        display_dimensions.height, display_dimensions.width)

    header = '{}\n<svg {}\n  {}>\n'.format(XML_INFO, SVG_INFO, height_width)
    return header


class Graphics:
    """
    Class for graphical output. 

    This version of the class generates SVG code and saves it to a
    file.
    """
    def __init__(self, display_dimensions: DisplayDimensions, colours): 
        """
        Parameters:
        display_dimensions -- The height and width of the display area.
        colours -- A list (or an object indexable in the same way as a
          list) containing strings representing colours e.g 'red',
          'rgb(46,41,51)'.
        """
        self._display_dimensions = display_dimensions
        self._colours = colours

        self._commands = ''
        self._polygon_count = 0

    def draw_polygon(self, points, fill_colour_index):
        """
        Parameters:
        points -- The x,y coordinates (Point instances) of the
          polygon's corners.        
        fill_colour_index -- Specifies which fill colour to use from
          the colours in the colours object passed to the
          constructor.
        """
        assert (self._polygon_count < MAX_POLYGONS), TOO_MANY_POLYGONS_ERR

        colour = self._colours[fill_colour_index]
        command = create_polygon_command(
            points, colour, self._display_dimensions.height)

        self._commands += command
        self._polygon_count += 1

    def save(self, path) -> Status:
        header = create_svg_header(self._display_dimensions)
        content = header + self._commands + '</svg>\n'

        status = Status(ok=True)
        try:
            with open(path, 'w') as svg_file:
                svg_file.write(content)
        except Exception as e:
            err_str = 'Error writing to {}: {}.'.format(path, str(e))
            status = Status(ok=False, err_str=err_str)
        return status
