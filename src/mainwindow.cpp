//
// Created by Ross Wardrup on 9/13/20.
//

#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) : QMainWindow(parent) {
    /*
     * Set up the main window.
     */
    ui.setupUi(this);

    // Set up menubar items
    QMenu *edit_menu = menuBar()->addMenu("Edit");
    auto *user_settings = new QAction("User Settings");
    edit_menu->addAction(user_settings);
}
