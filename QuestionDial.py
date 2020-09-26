# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QuestionDial.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(750, 750)
        self.choice2 = QtWidgets.QCheckBox(Dialog)
        self.choice2.setGeometry(QtCore.QRect(80, 290, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.choice2.setFont(font)
        self.choice2.setObjectName("choice2")
        self.choice4 = QtWidgets.QCheckBox(Dialog)
        self.choice4.setGeometry(QtCore.QRect(80, 450, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.choice4.setFont(font)
        self.choice4.setObjectName("choice4")
        self.Instructions = QtWidgets.QLabel(Dialog)
        self.Instructions.setGeometry(QtCore.QRect(30, 130, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        self.Instructions.setFont(font)
        self.Instructions.setObjectName("Instructions")
        self.choice1 = QtWidgets.QCheckBox(Dialog)
        self.choice1.setGeometry(QtCore.QRect(80, 210, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.choice1.setFont(font)
        self.choice1.setObjectName("choice1")
        self.defQuestions = QtWidgets.QLabel(Dialog)
        self.defQuestions.setGeometry(QtCore.QRect(10, 0, 281, 101))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.defQuestions.setFont(font)
        self.defQuestions.setObjectName("defQuestions")
        self.choice3 = QtWidgets.QCheckBox(Dialog)
        self.choice3.setGeometry(QtCore.QRect(80, 370, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.choice3.setFont(font)
        self.choice3.setObjectName("choice3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.choice2.stateChanged.connect(self.checkClick)

    def checkClick(self, Dialog):
        print("Correct")



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.choice2.setText(_translate("Dialog", "Choice 1"))
        self.choice4.setText(_translate("Dialog", "Choice 1"))
        self.Instructions.setText(_translate("Dialog", "Please select a choice"))
        self.choice1.setText(_translate("Dialog", "Choice 1"))
        self.defQuestions.setText(_translate("Dialog", "Definition: "))
        self.choice3.setText(_translate("Dialog", "Choice 1"))

    def inputChoice(self, Dialog, choice, text,):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        if choice == 1:
            self.choice1.setText(_translate("Dialog", text))
            self.choice1.adjustSize()
        if choice == 2:
            self.choice2.setText(_translate("Dialog", text))
            self.choice2.adjustSize()
        if choice == 3:
            self.choice3.setText(_translate("Dialog", text))
            self.choice3.adjustSize()
        if choice == 4:
            self.choice4.setText(_translate("Dialog", text))
            self.choice4.adjustSize()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
