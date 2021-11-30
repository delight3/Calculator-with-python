import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStyleFactory
from PyQt5.uic import loadUi


class Calculator(QWidget):

    def __init__(self) -> None:
        QWidget.__init__(self)
        loadUi('static/calcu.ui', self)

        self.initial_value = '0'  # Global variable for input

        self.buttonhandle()
        self.setWindowTitle('calculator')
        self.show()

    def buttonhandle(self):
        self.btn0.clicked.connect(lambda: self.addNum(0))
        self.btn1.clicked.connect(lambda: self.addNum(1))
        self.btn2.clicked.connect(lambda: self.addNum(2))
        self.btn3.clicked.connect(lambda: self.addNum(3))
        self.btn7.clicked.connect(lambda: self.addNum(7))
        self.btn8.clicked.connect(lambda: self.addNum(8))
        self.btn9.clicked.connect(lambda: self.addNum(9))
        self.btn4.clicked.connect(lambda: self.addNum(4))
        self.btn5.clicked.connect(lambda: self.addNum(5))
        self.btn6.clicked.connect(lambda: self.addNum(6))
        self.btn_decimal.clicked.connect(lambda: self.addNum('.'))

        # Working with maths operators
        self.btn_plus.clicked.connect(lambda: self.calculate('+'))
        self.btn_minus.clicked.connect(lambda: self.calculate('-'))
        self.btn_multiply.clicked.connect(lambda: self.calculate('x'))
        self.btn_division.clicked.connect(lambda: self.calculate('/'))
        self.btn_equal.clicked.connect(lambda: self.calculate('='))
        self.btn_percent.clicked.connect(lambda: self.calculate('%'))

        # working with maths functions
        self.btn_reciprocal.clicked.connect(lambda: self.math_signs('rec'))
        self.btn_squareNumber.clicked.connect(self.math_signs)
        self.btn_squareRoot.clicked.connect(lambda: self.math_signs('root'))
        self.btn_clearsymbol.clicked.connect(self.backSpace)
        self.btn_C.clicked.connect(self.clearAll)
        self.btn_CE.clicked.connect(self.clearOne)

    def backSpace(self):
        value = self.lblInput.text()
        if len(value) > 1:
            self.lblInput.setText(value[:-1])
        else:
            self.lblInput.setText('0')
        print(value)

    def clearAll(self):
        self.lblInput.setText('0')
        self.lblHolder.setText('')

    def clearOne(self):
        self.lblInput.setText('0')

    def calculate(self, sign):
        value = self.lblInput.text()
        holder = self.lblHolder.text()
        if sign != "=":
            if sign == "x":
                sign = '*'
            self.lblHolder.setText(holder + value + " " + sign)
            self.lblInput.setText('0')
        else:
            holder += value
            if '%' in holder:
                stat = holder.split('%')
                result = (float(stat[0]) / 100) * float(stat[1])
                self.lblInput.setText(outputer(result))
            else:
                self.lblInput.setText(outputer(eval(holder)))
            self.lblHolder.setText('')
            self.initial_value = '0'

    def math_signs(self, sign):
        try:
            value = float(self.lblInput.text())
            if sign == 'rec':
                msg = 1 / value
            elif sign == 'root':
                msg = eval(f"{value} ** 0.5")
            else:
                msg = eval(f"{value} ** 2")
            self.lblInput.setText(outputer(msg))
        except Exception as err:
            print("sign error:", err)

    def addNum(self, number):
        value = self.lblInput.text()
        value = value.replace(',', '')
        if len(value) <= 15:
            if self.initial_value == '0':
                print(self.initial_value)
                self.lblInput.setText(str(number))
                self.initial_value = str(number)
            else:
                try:
                    print(self.initial_value)
                    value += str(number)
                    self.lblInput.setText("{:,}".format(int(value)))
                except Exception as err:
                    print("Error Msg: ", err)

def outputer(number):
    num = float(number)
    if num.is_integer():
        num = int(number)
    return str(num)


app = QApplication(sys.argv)
app.setStyle('fusion')
print(QStyleFactory.keys())
delight = Calculator()
sys.exit(app.exec_())
