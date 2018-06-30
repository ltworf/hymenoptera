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

#include <iostream>

#include "board.h"
#include "pedina.h"


void Board::addInsect(insect_t insect, unsigned int count) {
    while (count--) {
        this->pedine.append(new Pedina(this, WHITE, insect));
        this->pedine.append(new Pedina(this, BLACK, insect));
    }
}

Board::Board(QObject *parent) : QObject(parent) {
    // Base game
    this->addInsect(BEE, 1);
    this->addInsect(SPIDER, 2);
    this->addInsect(ANT, 3);
    this->addInsect(GRASSHOPPER, 3);
    this->addInsect(BEETLE, 2);
    //TODO extensions
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

void Board::printBoard() {
    const char* invert = "\e[7m";
    const char* reset = "\e[0m";

    //Unplaced for player 1
    std::cout << invert << "Player 1" << "\n";

    for (int i = 0; i < pedine.size(); i++) {
        Pedina* p = pedine[i];
        if (!p->placed() && p->player() == WHITE)
            std::cout << p->symbol().toStdString();
    }
    std::cout << "\n";
    std::cout << reset;

    //Board
    //TODO

    //Unplaced for player 2
    std::cout << "Player 2" << "\n";

    for (int i = 0; i < pedine.size(); i++) {
        Pedina* p = pedine[i];
        if (!p->placed() && p->player() == BLACK)
            std::cout << p->symbol().toStdString();
    }
    std::cout << "\n";
}
