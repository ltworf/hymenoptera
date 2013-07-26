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
        self.bgcolor = 0xB00000
        pass
    
    def getQColorbg(self):
        r = (self.bgcolor & 0xFF0000) >> 16
        g = (self.bgcolor & 0x00FF00) >> 8
        b = self.bgcolor & 0x0000FF
        return QtGui.QColor(r,g,b)


class QHexagon(QtGui.QWidget):
    
    clicked = QtCore.pyqtSignal(int,int, name='clicked')
    
    def __init__(self):
        super(QHexagon, self).__init__()
        
        self.hexagons = {}
        
        self.hmax = 1
        self.vmax = 1
        
        self.voffset = 0
        self.hoffset = 0
        
    def _find_max_offset(self):
        
        minx = min(self.hexagons.keys(),key = lambda x: x[0])[0]
        maxx = max(self.hexagons.keys(),key = lambda x: x[0])[0]
        
        miny = min(self.hexagons.keys(),key = lambda x: x[1])[1]
        maxy = max(self.hexagons.keys(),key = lambda x: x[1])[1]
        
        self.hmax = abs(maxx-minx)+1
        self.vmax = abs(maxy-miny)+1
        
        if minx < 0:
            self.hoffset = -minx
        if miny < 0:
            self.voffset = -miny
        
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
    
    def mousePressEvent(self,ev):
        #self.clicked.emit(x,y)
        print (ev.x(),ev.y())

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        
        qp.begin(self)
        qp.setRenderHints(QtGui.QPainter.Antialiasing | QtGui.QPainter.TextAntialiasing)
        
        # Deciding zoom
        hradius = self.size().width() / (self.hmax * 10.0 / 11.0)
        vradius = self.size().height() / (self.vmax * 6.0 / 7.0)
        
        radius = float(min(hradius,vradius))/2
        apothem = math.sqrt(radius**2 - ((radius/2)**2))
        sside = math.sqrt((radius**2) - ( (apothem) **2))
        
        
        #color = QtGui.QColor(212, 212, 212)
        #qp.setPen(color)
        
        for i in self.hexagons.keys():
            x,y=i
            x+=self.hoffset
            y+=self.voffset
            
            
            hexagon = self.hexagons[i]

            qp.setBrush(hexagon.getQColorbg())
            
            if (y % 2 == 0):
                x = x*apothem*2 + apothem
                y = y*radius*2 + radius - ((y/2)*radius)
            else:
                x = x*apothem*2 + apothem*2
                
                y = y*radius*2+sside - ((y/2)*radius)
            
            x+=radius/2
            y+=radius/2
            h = self.hexagon(x,y,radius)
            qp.drawPolygon(h)
            
        qp.end()
        
        
def main():
    
    
    e = Hexagon()
    g = Hexagon()
    g.bgcolor = 0xFFFFFF
    
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
    
    ex.addHexagon(g,3,0)
    
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()