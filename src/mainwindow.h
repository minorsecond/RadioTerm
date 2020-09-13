//
// Created by Ross Wardrup on 9/13/20.
//

#ifndef RADIOTERM_MAINWINDOW_H
#define RADIOTERM_MAINWINDOW_H

#include <QMainWindow>
#include "ui_mainwindow.h"

class MainWindow : public QMainWindow {
Q_OBJECT
Ui::MainWindow ui{};

public:
    explicit MainWindow(QWidget *parent = nullptr);
};


#endif //RADIOTERM_MAINWINDOW_H
