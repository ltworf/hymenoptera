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

#ifndef PEDINA_H
#define PEDINA_H

#include <QObject>

#include "board.h"
#include "definitions.h"

class Pedina : public QObject
{
    Q_OBJECT
public:
    explicit Pedina(Board *board, player_t player, insect_t insect);

private:
    player_t player;
    insect_t insect;

signals:

public slots:
};

#endif // PEDINA_H
