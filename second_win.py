# напиши здесь код для второго экрана приложения

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,QHBoxLayout, QLineEdit
from instr import *
from final_win import *
from PyQt5.QtCore import Qt, QTimer, QTime


class TestWin(QWidget):
    def __init__ (self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.move(win_x, win_y)
        self.resize(win_width, win_height)
    def initUI(self):
        self.name = QLabel(txt_name)
        self.hintname = QLineEdit(txt_hintname)
        self.age = QLabel(txt_age)
        self.hintage = QLineEdit(txt_hintage)
        self.test = QLabel(txt_test1)
        self.begin = QPushButton(txt_starttest1)
        self.hinttest1 = QLineEdit(txt_hinttest1)
        self.test2 = QLabel(txt_test2)
        self.sit = QPushButton(txt_starttest2)
        self.test3 = QLabel(txt_test3)
        self.final = QPushButton(txt_starttest3)
        self.hinttest2 = QLineEdit(txt_hinttest2)
        self.hinttest3 = QLineEdit(txt_hinttest3)
        self.sendresults = QPushButton(txt_sendresults)
        self.txt_timer = QLabel(txt_timer)
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.l_line.addWidget(self.name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.hintname, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.hintage, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.begin, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.hinttest1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.sit, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.final, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.hinttest2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.hinttest3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.sendresults, alignment = Qt.AlignCenter)


        self.r_line.addWidget(self.txt_timer, alignment = Qt.AlignCenter)


        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def connects(self):
        self.sendresults.clicked.connect(self.next_click)
        self.btn_test1.clicked.connect(self.timer_test)

    def next_click(self):
        self.hide()
        self.next_win = FinalWin()

    def timer_test(self):
        time = QTime(0, 0, 0)
        self.timer = QTimer()
        self.time.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def timer1Event(self):
        

      











app = QApplication ([])
second_min = TestWin()
app.exec()