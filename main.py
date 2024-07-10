from instr import *
from second_win import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton,
                             QLabel)


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()

    def initUI(self):
        self.btn_next = QPushButton(txt_next)
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)

        layout = QVBoxLayout()
        layout.addWidget(self.hello_text, alignment=Qt.AlignLeft)
        layout.addWidget(self.instruction, alignment=Qt.AlignLeft)
        layout.addWidget(self.btn_next)

        self.setLayout(layout)
        self.connects()

    def next_click(self):
        self.tw = TestWin()
        self.hide()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)


def main():
    app = QApplication([])
    mw = MainWin()
    app.exec()


if __name__ == "__main__":
    main()


























































































































































































