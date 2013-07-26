#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# QHexagon
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



import sys
import math

from PyQt4 import QtGui, QtCore

class Hexagon(object):
    '''
    This class represents an hexagon object.
    They can be added/removed to the QHexagon widget.
    '''
    def __init__(self):
        pass


class QHexagon(QtGui.QWidget):
    
    def __init__(self):
        super(QHexagon, self).__init__()
        
        self.hexagons = {}
        
        self.hmax = 1
        self.vmax = 1
        
        self.voffset = 0
        self.hoffset = 0
        
    def _find_max_offset(self):
        
        #minx = self.hexagons.keys()[0]
        
        #miny
        #maxx
        #maxy
        
        #for x,y in self.hexagons.keys():
            
        pass
    
    def addHexagon(self,h,x,y):
        self.hexagons[(x,y)] = h
        self._find_max_offset()
    def delHexagon(self,x,y):
        del self.hexagons[(x,y)]
        self._find_max_offset()
    
    def hexagon(self,x,y,r):
        '''
        Returns a QPolygon representing an hexagon centered in x,y
        with radius r
        '''
        
        p = []
        
        for i in range(7):
            angle = 2 * math.pi / 6 * (i + 0.5)
            edge_x = x + r * math.cos(angle)
            edge_y = y + r * math.sin(angle)
            p.append(QtCore.QPoint(edge_x,edge_y))
        
        return QtGui.QPolygon(p)
    

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        
        
        
        qp.begin(self)
        qp.setRenderHints(QtGui.QPainter.Antialiasing | QtGui.QPainter.TextAntialiasing)
        
        #TODO
        hmax=3
        vmax=8
        
        
        # Deciding zoom
        hradius = self.size().width() / hmax
        vradius = self.size().height() / vmax
        
        radius = float(min(hradius,vradius))/2
        apothem = math.sqrt(radius**2 - ((radius/2)**2))
        sside = math.sqrt((radius**2) - ( (apothem) **2))
        
        print (radius,apothem,sside)
        
        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#d4d4d4')
        qp.setPen(color)
        
        for i in self.hexagons.keys():
            x,y=i
            
            #TODO stuff
            qp.setBrush(QtGui.QColor(200, 0, 0))
            
            print(x,y)
            
            if (y % 2 == 0):
                x = x*apothem*2 + apothem
                y = y*radius*2 + radius - ((y/2)*radius)
            else:
                x = x*apothem*2 + apothem*2
                
                y = y*radius*2+sside - ((y/2)*radius)
            
            h = self.hexagon(x,y,radius)
            qp.drawPolygon(h)
            
        qp.end()
        
        
def main():
    
    
    e = Hexagon()
    
    app = QtGui.QApplication(sys.argv)
    ex = QHexagon()
    
    ex.addHexagon(e,0,0)
    ex.addHexagon(e,1,0)
    ex.addHexagon(e,0,1)
    ex.addHexagon(e,1,1)
    ex.addHexagon(e,2,1)
    
    ex.addHexagon(e,0,2)
    ex.addHexagon(e,1,2)
    
    ex.addHexagon(e,0,3)
    ex.addHexagon(e,1,3)
    
    ex.addHexagon(e,1,4)
    ex.addHexagon(e,1,5)
    
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()