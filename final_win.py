# напиши здесь код третьего экрана приложения
# напиши здесь код основного приложения и первог
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from instr import *
class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.index = QLabel(txt_index)
        self.result = QLabel(txt_workheart)
        self.line = QVBoxLayout()
        self.line.addWidget(self.index, alignment = Qt.AlignCenter)
        self.line.addWidget(self.result, alignment = Qt.AlignCenter)
        self.setLayout(self.line)


