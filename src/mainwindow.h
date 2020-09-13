//
// Created by Ross Wardrup on 9/13/20.
//

#ifndef RADIOTERM_MAINWINDOW_H
#define RADIOTERM_MAINWINDOW_H

#include <QMainWindow>
#include "ui_mainwindow.h"

class MainWindow : public QMainWindow {
Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow() override;

private:
    Ui::MainWindow *ui;

private slots:
    static void open_user_settings_window();
};


#endif //RADIOTERM_MAINWINDOW_H
