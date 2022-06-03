import sys
from PyQt6.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import (QWidget, QMainWindow, QLineEdit, QLabel,
                             QHBoxLayout, QVBoxLayout, QPushButton, QApplication)
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        widget = MyWidget()
        self.setCentralWidget(widget)
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('My App')
        self.show()

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):


        self.lbl = QLabel(self)
        qle = QLineEdit(self)
        qle.textChanged[str].connect(self.onChanged)
        hbox = QVBoxLayout()
        hbox.addWidget(self.lbl)
        hbox.addWidget(qle)

        button1 = QPushButton('一键替换')
        button2 = QPushButton('退出')
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(button2)
        hbox2.addWidget(button1)


        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)

        self.setLayout(vbox)
        # self.setGeometry(300, 300, 350, 250)
        # self.setWindowTitle('My App')
        # self.show()
    def onChanged(self, text):

        self.lbl.setText(text)
        self.lbl.adjustSize()

def main():
    app = QApplication([])
    ex = MyApp()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()