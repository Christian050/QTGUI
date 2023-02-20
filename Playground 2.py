import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


app = QApplication(sys.argv)
win = QMainWindow()


win.setGeometry(0, 0, 500, 500)
win.setWindowIcon(QIcon('0001.jpg'))
win.setWindowTitle('Playground 2')


fr = QtWidgets.QFrame(win)
fr.setFixedHeight(500)
fr.setFixedWidth(500)
fr.setStyleSheet('background-image: url(0001.jpg);'
                 'background-repeat: no-repeat')


lb = QtWidgets.QLabel(fr)
lb.setText('Text In Frame')
lb.move(10, 50)

win.show()
sys.exit(app.exec_())
