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


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y


class Triangle:
    def __init__(self, corner0: Point, corner1: Point, corner2: Point):
        self.__corners = (corner0, corner1, corner2)
    
    @property
    def corners(self):
        return self.__corners

    def __getitem__(self, index):
        return self.corners[index]
    
    def __iter__(self):
        return iter(self.corners)


