import sys
import re
import os.path
from PyQt6.QtCore import QDate, QTime, QDateTime, Qt
from PyQt6.QtWidgets import (QWidget, QMainWindow, QLineEdit, QLabel,
                             QHBoxLayout, QMessageBox, QPushButton, QApplication, QGridLayout)
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        path = QLabel('文件夹路径')
        rep = QLabel('替换版本')
        self.pathEdit = QLineEdit()
        self.pathEdit.textChanged[str].connect(self.onChanged)
        self.repEdit = QLineEdit()
        self.repEdit.textChanged[str].connect(self.onChanged)
        grid.addWidget(path, 1, 0)
        grid.addWidget(self.pathEdit, 1, 1)

        grid.addWidget(rep, 2, 0)
        grid.addWidget(self.repEdit, 2, 1)

        button1 = QPushButton('一键替换')
        button1.clicked.connect(self.buttonClicked)
        qbtn = QPushButton('退出')
        qbtn.clicked.connect(QApplication.instance().quit)
        hbox = QHBoxLayout()
        hbox.addWidget(qbtn)
        hbox.addWidget(button1)
        grid.addLayout(hbox, 3,1)

        self.statusBar()
        self.path = ""
        self.version = ""
        widget = QWidget()
        self.setCentralWidget(widget)
        self.centralWidget().setLayout(grid)
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('My App')
        self.show()

    def onChanged(self, text):
        sender = self.sender()
        print(sender)
        if sender == self.pathEdit:
            print('path:' +text)
            self.path = text
        else :
            print('version:' + text)
            self.version = text


    def buttonClicked(self):
        msg = '路径是:' + self.path + ', 版本是:' + self.version
        if self.path == "":
            QMessageBox.warning(self, "警告", "路径不能为空！")
        elif self.version == "":
            QMessageBox.warning(self, "警告", "版本不能为空！")
        else:
            print(msg)
            self.statusBar().showMessage(msg)
            self.walkPath()

    def walkPath(self):
        if not os.path.exists(self.path):
            QMessageBox.warning(self, "警告", "非法路径！")
        if not re.match(r'[Vv][0-9].[0-9]+', self.version):
            QMessageBox.warning(self, "警告", "版本非法！")
        now = QDate.currentDate()
        self.date = now.toString(Qt.DateFormat.ISODate)
        self.date = re.sub('-', "", self.date)
        print(self.date)
        for parent, dirnames, filenames in os.walk(self.path):
            for filename in filenames:
                print(os.path.join(parent, filename))
                newName = re.sub(r'[Vv][0-9].[0-9]+', self.version, filename)
                newName = re.sub(r'[0-9]{8}', self.date, newName)
                print(os.path.join(parent, newName))
                #os.rename(os.path.join(parent, filename), os.path.join(parent, newName))


def main():
    app = QApplication([])
    ex = MyApp()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()