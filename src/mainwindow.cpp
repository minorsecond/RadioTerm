//
// Created by Ross Wardrup on 9/13/20.
//

#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "ui_user_settings.h"
#include "user_settings.h"

MainWindow::MainWindow(QWidget *parent) : QMainWindow(parent), ui(new Ui::MainWindow){
    /*
     * Set up the main window.
     */
    ui->setupUi(this);

    // Set up menubar items
    QMenu * menu = menuBar()->addMenu("Preferences");
    QAction* preferences_action = new QAction("User Settings");
    menu->addAction(preferences_action);

    // Slots
    connect(preferences_action, SIGNAL(triggered()), this, SLOT(open_user_settings_window()));
}

void MainWindow::open_user_settings_window() {
    /*
     * Open the user settings dialog window.
     */
    UserSettings user_settings = UserSettings(nullptr);
    user_settings.setModal(false);
    user_settings.exec();
}

MainWindow::~MainWindow() {

}
