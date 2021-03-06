#!/usr/bin/env python
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
        self.bgcolor = 0xFFFFFF
        self.fgcolor = 0xFFFFFF
        pass
    
    def _colorToQColor(self,c):
        r = (c & 0xFF0000) >> 16
        g = (c & 0x00FF00) >> 8
        b = c & 0x0000FF
        return QtGui.QColor(r,g,b)
    
    def getQColorbg(self):
        return self._colorToQColor(self.bgcolor)
    def getQColorfg(self):
        return self._colorToQColor(self.fgcolor)

class QHexagon(QtGui.QGraphicsView):
    
    clicked = QtCore.pyqtSignal(int,int, name='clicked')
    
    def __init__(self):        
        super(QHexagon, self).__init__()
        
        self.scene = QtGui.QGraphicsScene()
        
        self.setRenderHints( QtGui.QPainter.Antialiasing );
        
        self.setScene(self.scene)
        
        self.hexagons = {}
        
        self.hmax = 1
        self.vmax = 1
        
        self.voffset = 0
        self.hoffset = 0
        
        self.manual_zoom = False
        
        self.repaint()
        
    def _find_max_offset(self):
        
        minx = min(self.hexagons.keys(),key = lambda x: x[0])[0]
        maxx = max(self.hexagons.keys(),key = lambda x: x[0])[0]
        
        miny = min(self.hexagons.keys(),key = lambda x: x[1])[1]
        maxy = max(self.hexagons.keys(),key = lambda x: x[1])[1]
        
        self.hmax = abs(maxx-minx)+1
        self.vmax = abs(maxy-miny)+1
        
        self.hoffset = -minx
        self.voffset = -miny
        
    def addHexagon(self,h,x,y):
        self.hexagons[(x,y)] = h
        self._find_max_offset()
        
        self.repaint()
        
    def delHexagon(self,x,y):
        del self.hexagons[(x,y)]
        self._find_max_offset()
        
        self.repaint()
    
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
    
    def _find_center(self,pos):
        pass
    
    def mousePressEvent(self,ev):
        buttons = int(ev.buttons())
        print buttons
        
        
        if buttons  == QtCore.Qt.LeftButton:
            item = self.itemAt(ev.x(),ev.y())
            if item is None:
                return
            x = (item.data(0).toInt())[0]
            y = (item.data(1).toInt())[0]
            print(x,y)
            self.clicked.emit(x,y)
        elif buttons == QtCore.Qt.MidButton:
            self.manual_zoom = False
            self.repaint()
    
    def wheelEvent(self,ev):
        #Zoom
        if int(ev.modifiers()) == QtCore.Qt.ControlModifier:
            self.radius += ev.delta()/100
            self.manual_zoom = True
            self.repaint()
            
            return
        
        #Scroll
        
        if ev.orientation() == QtCore.Qt.Vertical:
            v = self.verticalScrollBar()
            if v.maximum() != v.minimum():
                v.setValue(v.value() - ev.delta()/20)
        else:
            v = self.horizontalScrollBar()
            if v.maximum() != v.minimum():
                v.setValue(v.value() - ev.delta()/20)

        

    def repaint(self):
        
        map(self.scene.removeItem,self.scene.items())
        
        # Deciding zoom
        if not self.manual_zoom:
            hradius = self.size().width() / (self.hmax * 10.0 / 11.0)
            vradius = self.size().height() / (self.vmax * 6.0 / 7.0)
            
            radius = float(min(hradius,vradius))/2
            self.radius = radius
        else:
            radius = self.radius
        
        apothem = math.sqrt(radius**2 - ((radius/2)**2))
        sside = math.sqrt((radius**2) - ( (apothem) **2))
        
        
        #color = QtGui.QColor(212, 212, 212)
        #qp.setPen(color)
        
        for j in xrange(-self.hoffset -1, self.hmax+4):
            for k in xrange(-self.voffset -1, self.vmax+2):
                
                i=(j,k)
                
                x,y=i
                x+=self.hoffset
                y+=self.voffset
            
                if i in self.hexagons:
                    hexagon = self.hexagons[i]
                else:
                    hexagon = Hexagon()

                brush = QtGui.QBrush(hexagon.getQColorbg())
                pen = QtGui.QPen(hexagon.getQColorfg())
            
                if (y % 2 == 0):
                    x = x*apothem*2 + apothem
                    y = y*radius*2 + radius - ((y/2)*radius)
                else:
                    x = x*apothem*2 + apothem*2
                    y = y*radius*2+sside - ((y/2)*radius)
            
                x+=radius/2
                y+=radius/2
                h = self.hexagon(x,y,radius)
            
                item = self.scene.addPolygon(QtGui.QPolygonF(h),pen,brush)
                item.setData(0,i[0])
                item.setData(1,i[1])
            
        
        
def main():
    
    
    e = Hexagon()
    e.bgcolor = 0xDA0000
    g = Hexagon()
    g.bgcolor = 0xFFFFFF
    
    app = QtGui.QApplication(sys.argv)
    ex = QHexagon()
    
    ex.addHexagon(e,3,5)
    ex.addHexagon(e,9,0)
    ex.addHexagon(e,9,1)
    ex.addHexagon(e,9,1)
    ex.addHexagon(e,10,1)
    
    ex.addHexagon(e,9,2)
    ex.addHexagon(e,11,2)
    
    ex.addHexagon(e,10,3)
    ex.addHexagon(e,9,3)
    
    ex.addHexagon(e,9,4)
    ex.addHexagon(e,9,5)
    
    ex.addHexagon(g,3,0)
    
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()