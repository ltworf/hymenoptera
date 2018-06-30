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

#ifndef BOARD_H
#define BOARD_H

#include <QObject>
#include <QList>

#include "definitions.h"

class Pedina;

class Board : public QObject
{
    Q_OBJECT
public:
    explicit Board(QObject *parent = nullptr);

    Q_PROPERTY(unsigned int move_counter READ move_counter NOTIFY move_counterChanged)
    Q_PROPERTY(player_t turn READ turn NOTIFY turnChanged)

    void printBoard();
public slots:
    player_t turn();
    unsigned int move_counter();
    bool bee_played(player_t);
private:
    QList<Pedina*> pedine;
    unsigned int _move_counter = 0;
    player_t _turn = WHITE;
    bool _bee_in_play[2] = {false, false};
    void addInsect(insect_t insect, unsigned int count);
private slots:
    void setBeePlayed(player_t);

signals:
    void turnChanged(player_t);
    void move_counterChanged(unsigned int);
    void bee_playedChanged(player_t);

};

#endif // BOARD_H
