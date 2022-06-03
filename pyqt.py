import sys
from PyQt6.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import (QWidget, QMainWindow, QLineEdit, QLabel,
                             QHBoxLayout, QVBoxLayout, QPushButton, QApplication, QGridLayout)
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
        grid = QGridLayout()
        grid.setSpacing(10)

        path = QLabel('文件夹路径')
        rep = QLabel('替换版本')
        pathEdit = QLineEdit()
        pathEdit.textChanged[str].connect(self.onChanged)
        repEdit = QLineEdit()
        grid.addWidget(path, 1, 0)
        grid.addWidget(pathEdit, 1, 1)

        grid.addWidget(rep, 2, 0)
        grid.addWidget(repEdit, 2, 1)

        button1 = QPushButton('一键替换')
        qbtn = QPushButton('退出')
        qbtn.clicked.connect(QApplication.instance().quit)
        hbox = QHBoxLayout()
        hbox.addWidget(qbtn)
        hbox.addWidget(button1)
        grid.addLayout(hbox, 3,1)

        self.setLayout(grid)
        # self.setGeometry(300, 300, 350, 250)
        # self.setWindowTitle('My App')
        # self.show()
    def onChanged(self, text):
        a = text
        # self.lbl.setText(text)
        # self.lbl.adjustSize()

def main():
    app = QApplication([])
    ex = MyApp()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()