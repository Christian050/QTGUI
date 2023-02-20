import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)
win = QMainWindow()

win.setGeometry(1200, 300, 300, 250)
win.setWindowTitle("First Window")
win.setStyleSheet("background-image: url(0001.jpg);"
                  "background-position: center;"
                  "background-repeat: no-repeat;")


def done():
    print('Button Pressed')
    if fn_entry.text().isalpha() and sn_entry.text().isalpha():
        print('Name:  ' + fn_entry.text())
        print('Surname: ' + sn_entry.text())
        if male_checkbox.isChecked() and not female_checkbox.isChecked():
            print("You're " + male_checkbox.text().lower())
        elif female_checkbox.isChecked() and not male_checkbox.isChecked():
            print("You're " + female_checkbox.text().lower())
        if not male_checkbox.isChecked() and not female_checkbox.isChecked():
            print("You didn't click any checkbox")
        elif male_checkbox.isChecked() and female_checkbox.isChecked():
            print("You selected both")
    elif fn_entry.text().isalnum() or fn_entry.text().isnumeric():
        print('Firstname Includes Numbers')
        fn_entry.setFocus()
    elif sn_entry.text().isalnum() or sn_entry.text().isnumeric():
        print('Username Includes Numbers')
        sn_entry.setFocus()


fn_label = QtWidgets.QLabel(win)
fn_label.setText('Enter your first name here: ')
fn_label.move(20, 50)
fn_label.setFixedWidth(200)

fn_entry = QtWidgets.QLineEdit(win)
fn_entry.move(170, 50)

sn_label = QtWidgets.QLabel(win)
sn_label.setText('Enter your surname here:')
sn_label.move(20, 90)
sn_label.setFixedWidth(200)

sn_entry = QtWidgets.QLineEdit(win)
sn_entry.move(170, 90)

male_checkbox = QtWidgets.QCheckBox(win)
male_checkbox.setText('Male')
male_checkbox.move(20, 130)
male_checkbox.setFixedWidth(200)

female_checkbox = QtWidgets.QCheckBox(win)
female_checkbox.setText('Female')
female_checkbox.move(20, 170)
female_checkbox.setFixedWidth(200)

ok_btn = QtWidgets.QPushButton(win)
ok_btn.setText('Ok')
ok_btn.clicked.connect(done)
ok_btn.move(170, 200)


win.show()
sys.exit(app.exec_())
