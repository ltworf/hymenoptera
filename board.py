# -*- coding: utf-8 -*-
# hymenoptera
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

from itertools import *

from enum import Enum
from extraiter import *

class Player(Enum):
    '''
    Enumerates the colors of the player
    '''
    BLACK = 1
    WHITE = -1

class Piece(Enum):
    BEE = 1
    SPIDER = 2
    BEETLE = 3
    GRASSHOPPER = 4
    ANT = 5
    
    #Extensions
    MOSQUITO = 6
    LADYBUG = 7
    #TODO PILLBUG = 8
    
    
'''    1 Queen Bee (Yellow-Gold)
2 Spiders (Brown)
2 Beetles (Purple)
3 Grasshoppers (Green)
3 Soldier Ants (Blue)
In addition, one or more of the expansion pieces may be optionally added to the game:
1 Mosquito (Gray)
1 Ladybug (Red)
1 Pill bug (Cyan)'''

class PlacingException(Exception):
    pass

INITIAL_STANDARD = {
    Piece.BEE : 1,
    Piece.SPIDER : 2,
    Piece.BEETLE : 2,
    Piece.GRASSHOPPER : 3,
    Piece.ANT : 3,
}

INITIAL_MOSQUITO = {Piece.MOSQUITO : 1}
INITIAL_LADYBUG = {Piece.LADYBUG : 1}

class Board(object):
    
    def __init__(self, initial):
        self.positions = {}
        
        self.turn = Player.WHITE
        
        self.unplayed = {} #Pieces that are out of the board for the moment
        self.unplayed[Player.WHITE] = dict(initial)
        self.unplayed[Player.BLACK] = dict(initial)
        
        #Counts the number of played turns
        self.played_turns = {
            Player.WHITE: 0,
            Player.BLACK: 0,
        } 
        
    def get_cell(self,pos):
        '''
        Returns the content of a cell
        
        pos = (x,y)
        '''
        if pos in self.positions:
            return self.positions[pos]
        else:
            return []
    
    def get_player(self,pos):
        '''
        Returns the color of a cell or None
        '''
        r = self.get_cell(pos)
        if r == []:
            return None
        else:
            return r[-1][1]
    
    
    
    def place(self,pos,player,piece):
        '''
        Place a piece in the specified position
        
        pos = (x,y) position for the piece
        player = player placing the piece
        piece = piece that is being placed
        
        If the piece can't be placed there, it will
        raise an exception.
        '''
        
        if self.get_cell(pos) != []:
            raise PlacingException('Cell occupied')
        
        if player != self.turn:
            raise PlacingException('Wrong player')
        
        #check availability of piece
        if piece not in self.unplayed[player] or self.unplayed[player][piece] == 0:
            raise PlacingException('Piece unavailable')
        
        #check queen placement limits
        if self.unplayed[player][Piece.BEE] > 0:
            if self.played_turns[player] == 4 and piece != Piece.BEE:
                raise PlacingException('Bee needs to be placed')
        
        if len(self.positions) > 1:
            n = tee(filter(lambda x: x is not None,map(self.get_player,get_adjacent(pos))))
            
            same = iterlen(tuple(filter(lambda x: x == player,n[0])))
            diff = iterlen(tuple(filter(lambda x: x != player,n[1])))
            
            if diff > 0 or same < 1:
                raise PlacingException('Impossible location')
        elif len(self.positions) == 1:
            #1st black needs to touch white
            n = tuple(filter(lambda x: x is not None,map(self.get_player,get_adjacent(pos))))
            if iterlen(n) == 0:
                raise PlacingException('Piece not placed next to another')
        
        # All checks out
        
        #Placing piece
        self.positions[pos] = [(piece,player)]
        
        #Counting turn
        self.played_turns[player] += 1
        
        #Removing piece from pool
        self.unplayed[player][piece] -= 1
        
        #Changing player
        self.turn = -player


    
def get_adjacent(pos):
    '''
    Returns an iterable of adjacent cells

    pos = (x,y)
    '''
    x,y=pos[0],pos[1]
    
    return ((x,y+1),
               (x,y-1),
               (x-1,y-1 if x%2==0 else y+1),
               (x-1,y),
               (x+1,y-1 if x%2==0 else y+1),
               (x+1,y))