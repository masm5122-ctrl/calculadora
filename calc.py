from PyQt5.QtWidgets import QMainWindow, QShortcut
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QKeySequence
from funcoes import somar

from funcoes import (
    somar, subtrair, multiplicar, dividir,
    porcentagem
    )


class CalcUI(QMainWindow):

    def __init__(self, **kwargs): 
        super().__init__(**kwargs)
        loadUi("calculadora_iphone.ui", self)
        self.show()

        self.num1 = 0
        self.num2 = 0
        self.selectedOperation = None
        self.operationList = {
            "+": somar,
            "-": subtrair,
            "x": multiplicar,
            "÷": dividir,

        }

        #QShortcut(QKeySequence("0"), self).activated.connect(lambda: self.addNumber(0))
        self.btn_1.clicked.connect(lambda: self.addNumber(1))
        self.btn_2.clicked.connect(lambda: self.addNumber(2))
        self.btn_3.clicked.connect(lambda: self.addNumber(3))
        self.btn_4.clicked.connect(lambda: self.addNumber(4))
        self.btn_5.clicked.connect(lambda: self.addNumber(5))
        self.btn_6.clicked.connect(lambda: self.addNumber(6))
        self.btn_7.clicked.connect(lambda: self.addNumber(7))
        self.btn_8.clicked.connect(lambda: self.addNumber(8))
        self.btn_9.clicked.connect(lambda: self.addNumber(9))
        self.btn_0.clicked.connect(lambda: self.addNumber(0))
        self.btn_virgula.clicked.connect( self.addComma)

        self.btn_maismenos.clicked.connect(self.invert)
        self.btn_limpar.clicked.connect(self.cleanDisplay)
        self.btn_igual.clicked.connect(self.showResult)
        self.btn_porcetagem.clicked.connect(self.porcent)

        self.btn_mais.clicked.connect(lambda:self.setOperation("+"))
        self.btn_menos.clicked.connect(lambda:self.setOperation("-"))
        self.btn_div.clicked.connect(lambda:self.setOperation("÷"))
        self.btn_mult.clicked.connect(lambda:self.setOperation("x"))


    def addComma(self):
        ultimo = self.display.text()
        if ultimo.count(",") > 0:
            resultado = ultimo
        else:
            resultado = ultimo + ","
        self.display.setText(resultado)


    def addNumber(self, numero):
        self.btn_limpar.setText("<=")
        ultimo = self.display.text()
        if ultimo == '0':
            resultado = str(numero)
        else:
            resultado = ultimo + str(numero)
        self.display.setText(resultado)

    def cleanDisplay(self):
        if self.btn_limpar.text() == "AC":
            self.display.setText("0")
            self.display2.setText("0")
            self.num2 = 0
        else:
            ultimo = self.display.text()[:-1]
            if len(ultimo) == 0:
                ultimo = "0"
                self.btn_limpar.setText("AC")
            self.display.setText(ultimo)
        

    def getNumberDisplay(self, display):
        num = display.text()
        if "," in num:
            num = num.replace(',','.')
            num = float(num)
        else:
            num = int(num)
        return(num)
    
    def setNumberDisplay(self, number):
        number = str(number)
        number = number.replace('.',',')
        self.display.setText(number)

    def setCalcDisplay(self, num1, num2, operation):
        num1 = str(num1).replace('.',',')
        num1 = str(num1).replace('.',',')
        result =f'{num1} {operation} {num2} ='
        self.display2.setText(result)

    def showResult(self):
        if self.num2 == 0:
            self.num2 = self.getNumberDisplay(self.display)

        num1 = self.num1
        num2 = self.num2

        operation_simbol = self.operationList.get(self.selectedOperation )
        result = operation_simbol(num1,num2)
        self.num1 = result

        self.setNumberDisplay(result)
        self.setCalcDisplay(num1, num2, self.selectedOperation)
        self.btn_limpar.setText("AC")
      

    def setOperation(self, operation_simbol:str):
        self.selectedOperation = operation_simbol
        self.num1 = self.getNumberDisplay(self.display)
        self.num2 = 0
        result = self.display.text()
        self.display2.setText(result)
        self.display.setText("0")

    def invert(self):
        numero = int(self.display.text())
        numero = str(numero * -1)
        self.display.setText(numero)

    def porcent(self):
        porc = self.getNumberDisplay(self.display)
        result = porcentagem (self.num1, porc)
        self.setNumberDisplay(result)
            


        

       




        