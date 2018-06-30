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
#ifndef DEFINITIONS_H
#define DEFINITIONS_H

typedef enum insect_t {
    //Base game
    BEE,
    ANT,
    GRASSHOPPER,
    SPIDER,
    BEETLE,
    //Extensions
    MOSQUITO,
    LADYBUG,
    PILLBUG,
} insect_t;

typedef enum player_t {
    BLACK = 1,
    WHITE = -1,
} player_t;

#endif // DEFINITIONS_H
