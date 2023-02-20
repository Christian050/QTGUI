import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)
win = QMainWindow()

win.setGeometry(1200, 300, 700, 700)
win.setWindowTitle('Lesson 3')


win.show()
sys.exit(app.exec_())
