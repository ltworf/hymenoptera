/*
 * This file is part of Hymenoptera
 * Copyright (C) 2018  Salvo "LtWorf" Tomaselli
 *
 * Hymenoptera is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * author Salvo "LtWorf" Tomaselli <tiposchi@tiscali.it>
 */


#include "board.h"

Board::Board(QObject *parent) : QObject(parent)
{

}

player_t Board::turn() {
    return this->_turn;
}

unsigned int Board::move_counter() {
    return this->_move_counter;
}

bool Board::bee_played(player_t player) {
    switch (player) {
    case WHITE:
        return this->_bee_in_play[0];
    case BLACK:
    default:
        return this->_bee_in_play[1];
    }
}

void Board::setBeePlayed(player_t player) {
    switch (player) {
    case WHITE:
        this->_bee_in_play[0] = true;
        break;
    case BLACK:
        this->_bee_in_play[1] = true;
        break;
    }
    emit bee_playedChanged(player);
}
