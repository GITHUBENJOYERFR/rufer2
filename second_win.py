from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, \
    QPushButton, QLabel, QLineEdit

from instr import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def initUI(self):
        self.name = QLabel(txt_name)
        self.btn_name = QLineEdit(txt_hintname)
        self.year = QLabel(txt_age)
        self.btn_age = QLineEdit(txt_hintage)
        self.instruct = QLabel(txt_test1)
        self.start_test = QPushButton(txt_starttest1)
        self.btn_test = QLineEdit(txt_hinttest1)
        self.instruct2 = QLabel(txt_test2)
        self.btn_test2 = QPushButton(txt_starttest2)
        self.instruct3 = QLabel(txt_test3)
        self.start_test2 = QPushButton(txt_starttest3)
        self.one = QLineEdit(txt_hinttest3)
        self.two = QLineEdit(txt_hinttest3)

        self.vlayout1 = QVBoxLayout()
        self.vlayout2 = QVBoxLayout()
        self.hlayout = QHBoxLayout()

        self.vlayout1.addWidget(self.name, alignment=Qt.AlignLeft)
        self.vlayout1.addWidget(self.btn_name, alignment=Qt.AlignLeft)
        self.vlayout1.addWidget(self.year, alignment=Qt.AlignLeft)
        self.vlayout1.addWidget(self.btn_age, alignment=Qt.AlignLeft)
        self.vlayout1.addWidget(self.instruct, alignment=Qt.AlignLeft)
        self.vlayout1.addWidget(self.start_test, alignment=Qt.AlignLeft)
        self.vlayout1.addWidget(self.btn_test, alignment=Qt.AlignLeft)
        self.vlayout1.addWidget(self.instruct2, alignment=Qt.AlignLeft)
        self.vlayout1.addWidget(self.btn_test2, alignment=Qt.AlignLeft)
        self.vlayout1.addWidget(self.instruct3, alignment=Qt.AlignLeft)
        self.vlayout1.addWidget(self.start_test2, alignment=Qt.AlignLeft)
        self.vlayout1.addWidget(self.one, alignment=Qt.AlignLeft)
        self.vlayout1.addWidget(self.two, alignment=Qt.AlignLeft)

        self.hlayout.addLayout(self.vlayout1)

        self.setLayout(self.hlayout)

    def timer_test(self):
        self.time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer1Event(self):
        self.time = self.time.addSecs(-1)
        self.text_timer.setText(self.time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if self.time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def connects(self):
        # Нужно определить атрибуты btn_next, btn_test1, btn_test2, btn_test3 и text_timer
        pass

    def next_click(self):
        self.tw = TestWin()
        self.hide()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)