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
        self.__height = height
        self.__width = width

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width


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
        colours -- A list (or other object whose elements can be
          accessed with the '[]' operator with an integer index)
          containing strings representing colours e.g 'red',
          'rgb(46,41,51)'.
        """
        self.__display_dimensions = display_dimensions
        self.__colours = colours

        self.__commands = ""
        self.__polygon_count = 0

    def draw_polygon(self, points, fill_colour_index):
        """
        Parameters:
        points -- The x,y coordinates (Point instances) of the
          polygon's corners.        
        fill_colour_index -- Specifies which fill colour to use from
          the colours in the colours object passed to the
          constructor.
        """
        assert (self.__polygon_count < MAX_POLYGONS), TOO_MANY_POLYGONS_ERR 

        point_strings = [self.__format_point(point) for point in points]
        points = " ".join(point_strings)
        command = "   <polygon points=\"{}\" style=\"fill:{}\"/>\n".format(
            points, self.__colours[fill_colour_index])

        self.__commands += command
        self.__polygon_count += 1

    def save(self, path) -> Status:
        height_width = "height=\"{:g}\" width=\"{:g}\"".format(
            self.__display_dimensions.height,
            self.__display_dimensions.width)
            
        header = "{}\n<svg {}\n     {}>\n".format(
            XML_INFO, SVG_INFO, height_width)
        footer = "</svg>\n"
        content = header + self.__commands + footer

        status = Status(ok=True)
        try:
            with open(path, "w") as svg_file:
                svg_file.write(content)
        except Exception as e:
            err_str = "Error writing to {}: {}.".format(path, str(e))
            status = Status(ok=False, err_str=err_str)
        return status
    
    def __format_point(self, point: Point):
        x = round(point.x)
        y = self.__display_dimensions.height - round(point.y)
        return "{:g},{:g}".format(x, y)




