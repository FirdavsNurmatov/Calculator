from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('calc')
        self.setFixedSize(300,350)

        self.text = '0'
        self.operators = False
        self.ans = False
        self.pnt = False

        self.first_line = QLineEdit()
        self.first_line.setFixedHeight(40)
        
        # Horizontal line
        self.h1_operators = QHBoxLayout()
        
        self.btn_AC = QPushButton('AC')
        self.btn_AC.setFixedSize(65,50)
        self.btn_AC.setStyleSheet('font-size: 15px')
        
        self.btn_bracket1 = QPushButton('(')
        self.btn_bracket1.setFixedSize(65,50)
        self.btn_bracket1.setStyleSheet('font-size: 15px')
        
        self.btn_bracket2 = QPushButton(')')
        self.btn_bracket2.setFixedSize(65,50)
        self.btn_bracket2.setStyleSheet('font-size: 15px')
        
        self.btn_multiplication = QPushButton('/')
        self.btn_multiplication.setFixedSize(65,50)
        self.btn_multiplication.setStyleSheet('font-size: 15px')

        self.h1_operators.addWidget(self.btn_AC)
        self.h1_operators.addWidget(self.btn_bracket1)
        self.h1_operators.addWidget(self.btn_bracket2)
        self.h1_operators.addWidget(self.btn_multiplication)
        
        self.h2_operators = QHBoxLayout()
        
        self.btn_7 = QPushButton('7')
        self.btn_7.setFixedSize(65,50)
        self.btn_7.setStyleSheet('font-size: 15px')
        
        self.btn_8 = QPushButton('8')
        self.btn_8.setFixedSize(65,50)
        self.btn_8.setStyleSheet('font-size: 15px')
        
        self.btn_9 = QPushButton('9')
        self.btn_9.setFixedSize(65,50)
        self.btn_9.setStyleSheet('font-size: 15px')
        
        self.btn_division = QPushButton('*')
        self.btn_division.setFixedSize(65,50)
        self.btn_division.setStyleSheet('font-size: 15px')

        self.h2_operators.addWidget(self.btn_7)
        self.h2_operators.addWidget(self.btn_8)
        self.h2_operators.addWidget(self.btn_9)
        self.h2_operators.addWidget(self.btn_division)
        
        self.h3_operators = QHBoxLayout()
        
        self.btn_4 = QPushButton('4')
        self.btn_4.setFixedSize(65,50)
        self.btn_4.setStyleSheet('font-size: 15px')
        
        self.btn_5 = QPushButton('5')
        self.btn_5.setFixedSize(65,50)
        self.btn_5.setStyleSheet('font-size: 15px')
        
        self.btn_6 = QPushButton('6')
        self.btn_6.setFixedSize(65,50)
        self.btn_6.setStyleSheet('font-size: 15px')
        
        self.btn_minus = QPushButton('-')
        self.btn_minus.setFixedSize(65,50)
        self.btn_minus.setStyleSheet('font-size: 15px')

        self.h3_operators.addWidget(self.btn_4)
        self.h3_operators.addWidget(self.btn_5)
        self.h3_operators.addWidget(self.btn_6)
        self.h3_operators.addWidget(self.btn_minus)
        
        self.h4_operators = QHBoxLayout()
        
        self.btn_1 = QPushButton('1')
        self.btn_1.setFixedSize(65,50)
        self.btn_1.setStyleSheet('font-size: 15px')
        
        self.btn_2 = QPushButton('2')
        self.btn_2.setFixedSize(65,50)
        self.btn_2.setStyleSheet('font-size: 15px')
        
        self.btn_3 = QPushButton('3')
        self.btn_3.setFixedSize(65,50)
        self.btn_3.setStyleSheet('font-size: 15px')
        
        self.btn_plus = QPushButton('+')
        self.btn_plus.setFixedSize(65,50)
        self.btn_plus.setStyleSheet('font-size: 15px')

        self.h4_operators.addWidget(self.btn_1)
        self.h4_operators.addWidget(self.btn_2)
        self.h4_operators.addWidget(self.btn_3)
        self.h4_operators.addWidget(self.btn_plus)


        self.h5_operators = QHBoxLayout()
        
        self.btn_cross_out = QPushButton('⌫')
        self.btn_cross_out.setFixedSize(65,50)
        self.btn_cross_out.setStyleSheet('font-size: 15px')
        
        self.btn_0 = QPushButton('0')
        self.btn_0.setFixedSize(65,50)
        self.btn_0.setStyleSheet('font-size: 15px')
        
        self.btn_point = QPushButton('.')
        self.btn_point.setFixedSize(65,50)
        self.btn_point.setStyleSheet('font-size: 15px')
        
        self.btn_equal = QPushButton('=')
        self.btn_equal.setFixedSize(65,50)
        self.btn_equal.setStyleSheet('font-size: 15px')

        self.h5_operators.addWidget(self.btn_cross_out)
        self.h5_operators.addWidget(self.btn_0)
        self.h5_operators.addWidget(self.btn_point)
        self.h5_operators.addWidget(self.btn_equal)


        # Vertical line
        self.v_box = QVBoxLayout()

        self.first_line.setText(self.text)
        self.v_box.addWidget(self.first_line)
        self.v_box.addLayout(self.h1_operators)
        self.v_box.addLayout(self.h2_operators)
        self.v_box.addLayout(self.h3_operators)
        self.v_box.addLayout(self.h4_operators)
        self.v_box.addLayout(self.h5_operators)
        
        self.setLayout(self.v_box)

        # click pattern
        self.btn_bracket1.clicked.connect(self.write_str)
        self.btn_bracket2.clicked.connect(self.write_str)

        self.btn_multiplication.clicked.connect(self.opr)
        self.btn_division.clicked.connect(self.opr)
        self.btn_minus.clicked.connect(self.opr)
        self.btn_plus.clicked.connect(self.opr)
        
        self.btn_point.clicked.connect(self.write_point)
        
        self.btn_9.clicked.connect(self.write_num)
        self.btn_8.clicked.connect(self.write_num)
        self.btn_7.clicked.connect(self.write_num)
        self.btn_6.clicked.connect(self.write_num)
        self.btn_5.clicked.connect(self.write_num)
        self.btn_4.clicked.connect(self.write_num)
        self.btn_3.clicked.connect(self.write_num)
        self.btn_2.clicked.connect(self.write_num)
        self.btn_1.clicked.connect(self.write_num)
        self.btn_0.clicked.connect(self.write_num)
        
        self.btn_AC.clicked.connect(self.delete_all)
        self.btn_cross_out.clicked.connect(self.remove_last_chr)
        self.btn_equal.clicked.connect(self.answer)
        
    def write_num(self):
        btn = self.sender()
        btn = btn.text()
        if self.ans and self.operators == False:
            self.text = btn
            self.first_line.setText(self.text)
            self.operators = False
        else:
            if int(btn) != 0 or len(self.text) >= 1:
                count = 0
                if btn == '.':
                    self.pnt = True
                    # self.first_line.setText(self.text)
                if int(self.text[0]) == 0:
                        if 1 < len(self.text) < 3:
                            if self.text[1] == '.':
                                self.text += btn
                                self.first_line.setText(self.text)
                                count+=1 # 0.5 + 0.2 = 0.7 
                        else:
                            self.text  = ''
                            # self.first_line.setText(self.text)
                            # count+=1
                elif self.operators:
                    if btn == '0':
                        self.text += btn
                        self.first_line.setText(self.text)
                        self.text = self.text[:-1]
                        count+=1
                        self.operators = False
                        # print(self.text)
                    else:
                        self.first_line.setText(self.text)
                if count == 0:
                    self.text += btn
                    self.first_line.setText(self.text)
                    self.operators = False

    def write_str(self):
        btn = self.sender()
        self.text += btn.text()
        self.first_line.setText(self.text)

    def answer(self):
        self.text = str(eval(self.text))
        self.first_line.setText(self.text)  
        # self.ans = True

    def opr(self):
        if self.operators == False:
            btn = self.sender()
            self.text += btn.text()
            self.first_line.setText(self.text)
            self.operators = True
            self.pnt = False
        else:
            x = self.sender()
            self.text = self.text[:-1]
            self.text += x.text()
            self.first_line.setText(self.text) 

    def delete_all(self):
        self.text = '0'
        self.first_line.setText(self.text)

    def remove_last_chr(self):
        if len(self.text) == 1:
            self.text = '0'
            self.first_line.setText(self.text)
        else:
            self.text = self.text[:-1]
            self.first_line.setText(self.text)

    def write_point(self):
        if self.operators == False and self.pnt == False:
            btn = self.sender()
            self.text += btn.text()
            self.first_line.setText(self.text)
            self.pnt = True

app = QApplication([])
win = Window()
win.show()
app.exec_()
