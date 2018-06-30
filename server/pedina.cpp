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

#include "pedina.h"

Pedina::Pedina(Board *board, player_t player, insect_t insect): QObject(board) {
    this->_player = player;
    this->_insect = insect;
}


player_t Pedina::player() {
    return this->_player;
}

insect_t Pedina::insect() {
    return this->_insect;
}

bool Pedina::placed() {
    return this->_placed;
}

QString Pedina::symbol() {
    const char *insects[] = {
        "🐝",
        "🐜",
        "🦗",
        "🕷",
        "🐛", //TODO find a better symbol
        "🦋", //TODO find a better symbol
        "🐞",
        "🦂", //TODO find a better symbol
    };
    return QString(insects[this->_insect]);
}
