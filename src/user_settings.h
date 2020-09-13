//
// Created by Ross Wardrup on 9/13/20.
//

#ifndef RADIOTERM_USER_SETTINGS_H
#define RADIOTERM_USER_SETTINGS_H

#include <QDialog>
#include "ui_user_settings.h"

class UserSettings : public QDialog, public Ui::Dialog {
    /*
     * UserSettings methods
     */

    Q_OBJECT
    Ui::Dialog ui{};

public:
    explicit UserSettings(QWidget *parent = nullptr);
};


#endif //RADIOTERM_USER_SETTINGS_H
