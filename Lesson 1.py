import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
# from PyQt5.QtGui import QIcon

##################################################################################
# CREATING WINDOW WITH FUNCTION AND CLICKED CONNECT
##################################################################################

# Set window and application
app = QApplication(sys.argv)
win = QMainWindow()

# title, geometry and tool tip (show's text when mouse is idle)
win.setWindowTitle("Sup B")
win.setGeometry(1200, 300, 700, 700)
win.setToolTip("You're a piece of shit")
# win.setWindowIcon(QIcon('#image name in project folder')


# Clicked command (button command)
def clicked():
    print('button clicked')    # everytime button is clicked it prints this out
    print('First Name: ' + firstname_entry.text())
    print("Surname: " + surname_entry.text())


# label
firstname_label = QtWidgets.QLabel(win)
firstname_label.setText('wth is your first name :')
firstname_label.move(50, 50)
firstname_label.setFixedWidth(200)

# entry
firstname_entry = QtWidgets.QLineEdit(win)
firstname_entry.move(200, 50)
firstname_entry.setFixedHeight(25)

surname_label = QtWidgets.QLabel(win)
surname_label.setText('tf is your surname :')
surname_label.move(50, 90)
surname_label.setFixedWidth(200)

surname_entry = QtWidgets.QLineEdit(win)
surname_entry.move(200, 90)
surname_entry.setFixedHeight(25)

# button
save_btn = QtWidgets.QPushButton(win)
save_btn.setText('Save')
save_btn.clicked.connect(clicked)
save_btn.move(250, 130)

win.show()
sys.exit(app.exec_())
