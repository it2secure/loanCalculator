from PyQt5.QtWidgets import *  
from PyQt5 import QtCore, QtGui  
from PyQt5.QtGui import *  
from PyQt5.QtCore import *  
import sys  
  
class Window(QMainWindow):    
    def __init__(self):  
        super().__init__()  
        self.setWindowTitle("وام")  
        self.wd_width = 400  
        self.wd_height = 500  
        self.setGeometry(100, 100, self.wd_width, self.wd_height)  
        self.UiComponents()  
        self.show()  
    def UiComponents(self):  
        heading = QLabel("محاسبه کننده وام", self)  
        heading.setGeometry(0, 10, 400, 60)  
        font = QFont('Times', 15)  
        font.setBold(True)  
        font.setItalic(True)  
        font.setUnderline(True)  
        heading.setFont(font)  
        heading.setAlignment(Qt.AlignCenter)  
        color = QGraphicsColorizeEffect(self)  
        color.setColor(Qt.darkCyan)  
        heading.setGraphicsEffect(color)  
        int_label = QLabel("سود سالانه", self)  
        int_label.setAlignment(Qt.AlignCenter)  
        int_label.setGeometry(200, 100, 180, 40)   
        int_label.setStyleSheet("QLabel"  
                            "{"  
                            "border : 2px solid black;"  
                            "background : rgba(70, 70, 70, 35);"  
                            "}")  
        int_label.setFont(QFont('Times', 9))  
        self.rate = QLineEdit(self)  
        intOnly = QIntValidator()  
        self.rate.setValidator(intOnly)  
        self.rate.setGeometry(20, 100, 170, 40)
        self.rate.setAlignment(Qt.AlignCenter)  
        self.rate.setFont(QFont('Times', 9))  
        num_label = QLabel("چند ساله ", self)  
        num_label.setAlignment(Qt.AlignCenter)  
        num_label.setGeometry(200, 150, 180, 40) 
        num_label.setStyleSheet("QLabel"  
                            "{"  
                            "border : 2px solid black;"  
                            "background : rgba(70, 70, 70, 35);"  
                            "}")  
        num_label.setFont(QFont('Times', 9))  
        self.years = QLineEdit(self)   
        intOnly = QIntValidator()  
        self.years.setValidator(intOnly)  
        self.years.setGeometry(20, 150, 170, 40)   
        self.years.setAlignment(Qt.AlignCenter)  
        self.years.setFont(QFont('Times', 9))  
        amt_label = QLabel("مقدار پول", self)  
        amt_label.setAlignment(Qt.AlignCenter)  
        amt_label.setGeometry(200, 200, 180, 40)    
        amt_label.setStyleSheet("QLabel"  
                            "{"  
                            "border : 2px solid black;"  
                            "background : rgba(70, 70, 70, 35);"  
                              "}")  
        amt_label.setFont(QFont('Times', 9))  
        self.amount = QLineEdit(self)  
        intOnly = QIntValidator()  
        self.amount.setValidator(intOnly)  
        self.amount.setGeometry(20, 200, 170, 40)
        self.amount.setAlignment(Qt.AlignCenter)  
        self.amount.setFont(QFont('Times', 9))  
        calc = QPushButton("محاسبه پرداخت", self)  
        calc.setGeometry(125, 270, 150, 40)  
        calc.clicked.connect(self.calc_action)  
        self.mp_payment = QLabel(self)  
        self.mp_payment.setAlignment(Qt.AlignCenter)  
        self.mp_payment.setGeometry(50, 340, 300, 60)  
        self.mp_payment.setStyleSheet("QLabel"  
                                    "{"  
                                    "border : 3px solid black;"  
                                    "background : white;"  
                                    "}")  
        self.mp_payment.setFont(QFont('Arial', 11))  
        self.yp_payment = QLabel(self)  
        self.yp_payment.setAlignment(Qt.AlignCenter)  
        self.yp_payment.setGeometry(50, 410, 300, 60)  
        self.yp_payment.setStyleSheet("QLabel"  
                                    "{"  
                                    "border : 3px solid black;"  
                                    "background : white;"  
                                    "}")  
        self.yp_payment.setFont(QFont('Arial', 11))  
    def calc_action(self):  
        annualIntrstRate = self.rate.text()  
        if len(annualIntrstRate) == 0 or annualIntrstRate == '0':  
            return  
        numOfYrs = self.years.text()  
        if len(numOfYrs) == 0 or numOfYrs == '0':  
            return  
        loanAmt = self.amount.text()  
        if len(loanAmt) == 0 or loanAmt == '0':  
            return  
        annualIntrstRate = int(annualIntrstRate)  
        numOfYrs = int(numOfYrs)  
        loanAmt = int(loanAmt)  
        mnthlyIntrstRate = annualIntrstRate / 1200  
        mnthlyPaymnt = loanAmt * mnthlyIntrstRate / (1 - 1 / (1 + mnthlyIntrstRate) ** (numOfYrs * 12))  
        mnthlyPaymnt = "{:.3f}".format(mnthlyPaymnt)  
        self.mp_payment.setText("پرداخت ماهانه : " + str(mnthlyPaymnt))  
        ttlPayment = float(mnthlyPaymnt) * 12 * numOfYrs  
        ttlPayment = "{:.3f}".format(ttlPayment)  
        self.yp_payment.setText("مبلغ کل قابل پرداخت : " + str(ttlPayment))  

base = QApplication(sys.argv)  
window = Window()  
sys.exit(base.exec())  
