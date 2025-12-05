from PyQt5.QtWidgets import QMainWindow, QShortcut
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot, QTimer
from PyQt5.QtGui import QKeySequence


from funcoes import (
    somar, subtrair, multiplicar, dividir,
    porcentagem
    )

from os import path
import sys

def loadFile(file):
    base_path = getattr(sys, "_MEIPASS", path.dirname(path.abspath(__file__)))
    return path.join(base_path, file)


class CalcUI(QMainWindow):

    def __init__(self, **kwargs): 
        super().__init__(**kwargs)
        loadUi(loadFile("calculadora_iphone.ui"), self)
        self.show()

        self.num1 = 0
        self.num2 = 0
        self.finish = False

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
        if ultimo == '0' or self.finish :
            self.finish = False
            resultado = str(numero)
        else:
            resultado = ultimo + str(numero)
        self.display.setText(resultado)

    def cleanDisplay(self):
        if self.btn_limpar.text() == "AC":
            self.display.setText("0")
            self.display2.setText("0")
            self.num1 = 0
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
        if self.selectedOperation:
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
            self.finish = True
            if isinstance(result, str):
                self.timerClean()
        
    def setOperation(self, operation_simbol:str):
        self.selectedOperation = operation_simbol
        self.num1 = self.getNumberDisplay(self.display)
        self.num2 = 0
        result = self.display.text()
        self.display2.setText(result)
        self.display.setText("0")

    def invert(self):
        numero = self.getNumberDisplay(self.display)
        numero = str(numero * -1)
        self.setNumberDisplay(numero)

    def porcent(self):
        porc = self.getNumberDisplay(self.display)
        result = porcentagem (self.num1, porc)
        self.setNumberDisplay(result)
            
    def timerClean(self):
        self.btn_mais.setEnabled(False)
        self.btn_menos.setEnabled(False)
        self.btn_mult.setEnabled(False)
        self.btn_div.setEnabled(False)
        self.btn_maismenos.setEnabled(False)
        self.btn_porcetagem.setEnabled(False)
        self.btn_igual.setEnabled(False)

        self.cronometro = QTimer(self)
        self.cronometro.singleShot(1000, self.timeOutClean)

    def timeOutClean(self):
        self.btn_mais.setEnabled(True)
        self.btn_menos.setEnabled(True)
        self.btn_mult.setEnabled(True)
        self.btn_div.setEnabled(True)
        self.btn_maismenos.setEnabled(True)
        self.btn_porcetagem.setEnabled(True)
        self.btn_igual.setEnabled(True)
        self.display.setText("0")
        self.display2.setText("0")
        self.num1 = 0
        self.num2 = 0
        self.selectedOperation = None
    



        

       




        