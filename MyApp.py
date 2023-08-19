from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

"""
<Calculator App>
Theme from "https://colorhunt.co/palette/252b484450695b9a8bf7e987"
colors = ['#252B48', '#445069', '#F7E987']
"""

# forming mainwindow.
class MainWindow(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    # Return error message
    def initUI(self) -> None:
        self.setWindowTitle("Calculator")
        self.setGeometry(700, 300, 350, 510)
        self.setFixedSize(QSize(350, 510))
        self.setAutoFillBackground(True)
        mainPal = QPalette()
        mainPal.setColor(QPalette.Background, QColor("#252B48"))
        self.setPalette(mainPal)

        OUTPUT = self.createEditLine()
        INPUT = self.createKeyBoard()

        mainFrame = QVBoxLayout()
        mainFrame.addWidget(OUTPUT)
        mainFrame.addLayout(INPUT)

        self.setLayout(mainFrame)

        # show window.
        self.show()
    
    def createEditLine(self) -> QVBoxLayout:
        box = QGroupBox()
        box.setStyleSheet("color: white;"
                          "background-color: #252B48;"
                          "border: none;"
                          "border-radius: 2px;")

        inputline = QHBoxLayout()
        self.inputLabel = QLabel("INPUT : ")
        self.inputLabel.setStyleSheet("color: white;")
        inputFont = self.inputLabel.font()
        inputFont.setPointSize(10)
        inputFont.setFamily("Arial")
        inputFont.setBold(True)
        self.inputLabel.setFont(inputFont)

        self.inputbox = QLineEdit()
        self.inputbox.textChanged[str].connect(self.lineInputChanged)
        self.inputbox.setStyleSheet("color: white;"
                                    "background-color: #445069;"
                                    "border: none;"
                                    "border-bottom: 2px solid #F7E987;"
                                    "border-radius: 2px;"
                                    "font-family: Arial;")
        self.inputbox.setFixedSize(230, 40)
        inputline.addWidget(self.inputLabel)
        inputline.addWidget(self.inputbox)

        codeline = QHBoxLayout()
        self.codeLabel = QLabel("CODE : ")
        self.codeLabel.setStyleSheet("color: white;")
        codeFont = self.codeLabel.font()
        codeFont.setPointSize(10)
        codeFont.setFamily("Arial")
        codeFont.setBold(True)
        self.codeLabel.setFont(codeFont)

        self.codebox = QLineEdit()
        self.codebox.textChanged[str].connect(self.lineCodeChanged)
        self.codebox.setStyleSheet("color: white;"
                                    "background-color: #445069;"
                                    "border: none;"
                                    "border-bottom: 2px solid #F7E987;"
                                    "border-radius: 2px;"
                                    "font-family: Arial;")
        self.codebox.setFixedSize(230, 40)
        codeline.addWidget(self.codeLabel)
        codeline.addWidget(self.codebox)

        vertical_lines = QVBoxLayout()
        vertical_lines.addLayout(inputline)
        vertical_lines.addLayout(codeline)

        box.setFixedSize(325, 110)
        box.setLayout(vertical_lines)

        return box
    
    def createKeyBoard(self) -> QVBoxLayout:
        self.k_0 = QPushButton("0")
        self.k_1 = QPushButton("1")
        self.k_2 = QPushButton("2")
        self.k_3 = QPushButton("3")
        self.k_4 = QPushButton("4")
        self.k_5 = QPushButton("5")
        self.k_6 = QPushButton("6")
        self.k_7 = QPushButton("7")
        self.k_8 = QPushButton("8")
        self.k_9 = QPushButton("9")

        self.k_plus = QPushButton("+")
        self.k_minus = QPushButton("-")
        self.k_multiple = QPushButton("×")
        self.k_divide = QPushButton("÷")

        self.k_equal = QPushButton("=")
        self.k_C = QPushButton("C")
        self.k_dot = QPushButton(".")
        self.k_backspace = QPushButton("←")
        self.k_parentheses_ = QPushButton("(")
        self.k_parentheses = QPushButton(")")

        self.k_square = QPushButton("²")
        self.k_root = QPushButton(r"/")
        self.k_factorial = QPushButton("%")
        self.k_reverse = QPushButton("⁻¹")

        self.keyLayout = [[self.k_parentheses_, self.k_parentheses, self.k_C, self.k_backspace],
                          [self.k_square, self.k_root, self.k_factorial, self.k_divide],
                          [self.k_7, self.k_8, self.k_9, self.k_multiple],
                          [self.k_4, self.k_5, self.k_6, self.k_minus],
                          [self.k_1, self.k_2, self.k_3, self.k_plus],
                          [self.k_reverse, self.k_0, self.k_dot, self.k_equal]]
        
        self.keyDef = [[self.get_parentheses_, self.get_parentheses, self.get_C, self.get_backspace],
                          [self.get_square, self.get_root, self.get_factorial, self.get_divide],
                          [self.get_7, self.get_8, self.get_9, self.get_multiple],
                          [self.get_4, self.get_5, self.get_6, self.get_minus],
                          [self.get_1, self.get_2, self.get_3, self.get_plus],
                          [self.get_reverse, self.get_0, self.get_dot, self.get_equal]]
        
        keyboard = QVBoxLayout()
        for line in self.keyLayout:
            Line = QHBoxLayout()
            for element in line:
                Line.addWidget(element)
                element.setMaximumSize(90, 50)
            keyboard.addLayout(Line)
        
        for btns, fncs in zip(self.keyLayout, self.keyDef):
            for btn, fnc in zip(btns, fncs):
                btn.clicked.connect(fnc)
                btn.setStyleSheet("color: white;"
                                  "background-color: #445069;"
                                  "border-radius: 5px;"
                                  "font-family: Arial;")

        return keyboard
    
    def lineInputChanged(self, changed) -> None:
        formula = str(changed)
        self.inputbox.setText(formula)
        self.codebox.setText(formula)
    
    def lineCodeChanged(self, changed) -> None:
        formula = str(changed)
        self.codebox.setText(formula)
        formula = formula.replace("^(2)", "²")
        formula = formula.replace(r"/", "÷")
        formula = formula.replace("*", "×")
        formula = formula.replace("^(-1)", "⁻¹")
        self.inputbox.setText(formula)
    
    def updateOutput(self, key: str) -> None:
        before: str = self.inputbox.text()
        if key[0] == "*":
            # command
            command = key[1:]
            if command[0] == "b" and len(before) > 0:
                self.inputbox.setText(before[0:len(before)-1])
            elif command[0] == "C":
                self.inputbox.setText("")
            elif command[0] == "e":
                real_formula = self.codebox.text()
                result = self.calculate(real_formula)
                self.inputbox.setText(result) # update delay
        else:
            self.inputbox.setText(before+key)
        
        formula = self.inputbox.text()
        self.updateCodeOutput(formula)
    
    def updateCodeOutput(self, formula) -> None:
        formula = formula.replace("²", "^(2)")
        formula = formula.replace("÷", r"/")
        formula = formula.replace("×", "*")
        formula = formula.replace("⁻¹", "^(-1)")
        
        self.codebox.setText(formula)
    
    def keyPressEvent(self, e) -> None:
        if e.key() == Qt.Key_0: inkey = 0
        elif e.key() == Qt.Key_1: inkey = 1
        elif e.key() == Qt.Key_2: inkey = 2
        elif e.key() == Qt.Key_3: inkey = 3
        elif e.key() == Qt.Key_4: inkey = 4
        elif e.key() == Qt.Key_5: inkey = 5
        elif e.key() == Qt.Key_6: inkey = 6
        elif e.key() == Qt.Key_7: inkey = 7
        elif e.key() == Qt.Key_8: inkey = 8
        elif e.key() == Qt.Key_9: inkey = 9
        elif e.key() == Qt.Key_Control: inkey = "*C"
        elif e.key() == Qt.Key_ParenLeft: inkey = "("
        elif e.key() == Qt.Key_ParenRight: inkey = ")"
        elif e.key() == Qt.Key_Backspace: inkey = "*backspace"
        elif e.key() == Qt.Key_Percent: inkey = "%"
        elif e.key() == Qt.Key_Minus: inkey = "-"
        elif e.key() == Qt.Key_Plus: inkey = "+"
        elif e.key() == Qt.Key_Equal: inkey = "*equal"
        elif e.key() == Qt.Key_Return: inkey = "*equal"
        elif e.key() == Qt.Key_Enter: inkey = "*equal"
        elif e.key() == Qt.Key_Delete: inkey = "*backspace"
        
        try:
            self.updateOutput(str(inkey))
        except:
            ...

    def calculate(self, formula) -> str:
        try:
            formula = formula.replace("^", "**")
            get = str(eval(formula))
        except:
            get = "#Error"
        finally:
            return get

    def get_parentheses_(self): self.updateOutput("(")
    def get_parentheses(self): self.updateOutput(")")
    def get_C(self): self.updateOutput("*C")
    def get_backspace(self): self.updateOutput("*backspace")
    def get_square(self): self.updateOutput("²")
    def get_root(self): self.updateOutput(r"/")
    def get_factorial(self): self.updateOutput("%")
    def get_divide(self): self.updateOutput("÷")
    def get_7(self): self.updateOutput("7")
    def get_8(self): self.updateOutput("8")
    def get_9(self): self.updateOutput("9")
    def get_multiple(self): self.updateOutput("×")
    def get_4(self): self.updateOutput("4")
    def get_5(self): self.updateOutput("5")
    def get_6(self): self.updateOutput("6")
    def get_minus(self): self.updateOutput("-")
    def get_1(self): self.updateOutput("1")
    def get_2(self): self.updateOutput("2")
    def get_3(self): self.updateOutput("3")
    def get_plus(self): self.updateOutput("+")
    def get_reverse(self): self.updateOutput("⁻¹")
    def get_0(self): self.updateOutput("0")
    def get_dot(self): self.updateOutput(".")
    def get_equal(self): self.updateOutput("*equal")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())