# -*- coding: utf-8 -*-
# Enum
# Copyright (C) 2013  Salvo "LtWorf" Tomaselli
# 
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 
# author Salvo "LtWorf" Tomaselli <tiposchi@tiscali.it>

class EnumException(Exception):
    pass

class Enum(object):
    '''
    Represents an enum
    
    all the values should be defined as class attributes,
    and the class should never be instantiated.
    '''
    
    @classmethod
    def getdef(cls,val):
        '''
        Returns the corresponding definition to the given value
        
        raises EnumException if the value does not correspond to
        anything.
        It automatically skips hidden fields starting with _
        '''
        
        for i in dir(cls):
            if i.startswith('_'):
                continue
            if getattr(cls,i) == val:
                return i
        raise EnumException('Value not present in enum')