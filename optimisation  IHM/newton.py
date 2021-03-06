# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newton.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from Newton_Raphson import Derivé, fonction, newtonRaphson







class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(831, 620)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(680, 250, 111, 71))
        self.b1.setStyleSheet("background-color: rgb(255, 40, 52);\n"
"font: 24pt \"Arial Black\";\n"
"color: rgb(246, 255, 238);")
        self.b1.setObjectName("b1")
        self.line_a = QtWidgets.QLineEdit(self.centralwidget)
        self.line_a.setGeometry(QtCore.QRect(110, 240, 113, 21))
        self.line_a.setStyleSheet("")
        self.line_a.setText("")
        self.line_a.setObjectName("line_a")
        self.lineEdit_b = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_b.setGeometry(QtCore.QRect(300, 240, 113, 21))
        self.lineEdit_b.setStyleSheet("")
        self.lineEdit_b.setObjectName("lineEdit_b")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 40, 501, 61))
        self.label.setStyleSheet("color: rgb(255, 100, 95);\n"
"font: 48pt \".AppleSystemUIFont\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 751, 71))
        self.label_2.setStyleSheet("font: 48pt \".AppleSystemUIFont\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 170, 61, 61))
        self.label_3.setStyleSheet("font: 48pt \".AppleSystemUIFont\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(330, 170, 71, 61))
        self.label_4.setStyleSheet("font: 48pt \".AppleSystemUIFont\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(500, 170, 61, 61))
        self.label_5.setStyleSheet("font: 48pt \".AppleSystemUIFont\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(680, 350, 111, 61))
        self.label_6.setStyleSheet("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(650, 400, 161, 61))
        self.label_7.setStyleSheet("font: 15pt \".AppleSystemUIFont\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(680, 450, 111, 61))
        self.label_8.setStyleSheet("font: 20pt \".AppleSystemUIFont\";")
        self.label_8.setObjectName("label_8")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(70, 270, 541, 251))
        self.textEdit.setStyleSheet("")
        self.textEdit.setObjectName("textEdit")
        self.line_c = QtWidgets.QLineEdit(self.centralwidget)
        self.line_c.setGeometry(QtCore.QRect(470, 240, 113, 21))
        self.line_c.setStyleSheet("")
        self.line_c.setText("")
        self.line_c.setObjectName("line_c")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(560, 530, 261, 41))
        self.label_9.setStyleSheet("font: 20pt \".AppleSystemUIFont\";")
        self.label_9.setObjectName("label_9")
        self.b1_retour = QtWidgets.QPushButton(self.centralwidget)
        self.b1_retour.setGeometry(QtCore.QRect(710, 30, 101, 61))
        self.b1_retour.setStyleSheet("background-color: rgb(255, 40, 52);\n"
"font: 24pt \"Arial Black\";\n"
"color: rgb(246, 255, 238);")
        self.b1_retour.setObjectName("b1_retour")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 831, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.b1.setText(_translate("MainWindow", "Calcule"))
        self.label.setText(_translate("MainWindow", "*** Newton Raphson ***"))
        self.label_2.setText(_translate("MainWindow", "La fonction : 𝑓 = 𝑥³ − 7𝑥² + 8𝑥 − 3"))
        self.label_3.setText(_translate("MainWindow", "x0 "))
        self.label_4.setText(_translate("MainWindow", "ε"))
        self.label_5.setText(_translate("MainWindow", "N"))
        self.label_6.setText(_translate("MainWindow", "ε = epsilon"))
        self.label_7.setText(_translate("MainWindow", "N = nbr max d\'iteration"))
        self.label_8.setText(_translate("MainWindow", "x0 = initiale"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "SASSI Youssef ITS 2"))
        self.b1_retour.setText(_translate("MainWindow", "retour"))

        self.b1.clicked.connect(self.execute)


        
    


    def fonction(x):
        return x**3 - 7*(x**2) + 8*x- 9

    def Derivé(x):
        return 3*x**2 - 14*x + 8

    def newtonRaphson(x0_initial,e,N):
        
        step = 1
        i = 1
        condition = True
        while condition:
            try:
                if Derivé(x0_initial) == 0.0:
                    print('Divide by zero error!')
                    break

            except ZeroDivisionError:
                print("try again")
            x_suivante = x0_initial - fonction(x0_initial)/Derivé(x0_initial)
            print('X-%d, X= %0.6f -------- fonction(x) = %0.6f' % (step, x_suivante,fonction(x_suivante)))
            x0_initial = x_suivante
            step = step + 1

            if step > N:
                i = 0
                break
            condition = abs(fonction(x_suivante)) > e
    
        if i==1:
            print('\nRequired root is: %0.8f' % x_suivante)
            print('notre solution c\'est X=',step-1)
        else:
            print('\nil y a encore d iteration essaye de mettre plus de nombre pour N.')

    def execute(self):
        x0_initial = self.line_a.text()
        e = self.lineEdit_b.text()
        N = self.line_c.text()


# Converting x0_initial et e to float
        x0_initial = float(x0_initial)
        e = float(e)

# Converting N to integer
        N = int(N)
       
    
        
        

        newtonRaphson(x0_initial,e,N)

    
# Starting Newton Raphson Method
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    sys.exit(app.exec_())
