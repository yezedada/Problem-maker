# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\python\做题助手\UiMain_work_1_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1129, 579)
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 20, 321, 261))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setGeometry(QtCore.QRect(40, 40, 71, 16))
        self.label.setObjectName("label")
        self.L_all = QtWidgets.QLabel(self.groupBox_4)
        self.L_all.setGeometry(QtCore.QRect(120, 40, 72, 15))
        self.L_all.setText("")
        self.L_all.setObjectName("L_all")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(40, 90, 71, 16))
        self.label_3.setObjectName("label_3")
        self.L_have = QtWidgets.QLabel(self.groupBox_4)
        self.L_have.setGeometry(QtCore.QRect(120, 90, 72, 15))
        self.L_have.setText("")
        self.L_have.setObjectName("L_have")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(40, 140, 71, 16))
        self.label_5.setObjectName("label_5")
        self.L_will = QtWidgets.QLabel(self.groupBox_4)
        self.L_will.setGeometry(QtCore.QRect(120, 140, 72, 15))
        self.L_will.setText("")
        self.L_will.setObjectName("L_will")
        self.P_cent = QtWidgets.QProgressBar(self.groupBox_4)
        self.P_cent.setGeometry(QtCore.QRect(110, 190, 191, 20))
        self.P_cent.setProperty("value", 0)
        self.P_cent.setObjectName("P_cent")
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setGeometry(QtCore.QRect(40, 190, 71, 16))
        self.label_6.setObjectName("label_6")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(340, 280, 771, 181))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.RB_A = QtWidgets.QRadioButton(self.groupBox_2)
        self.RB_A.setGeometry(QtCore.QRect(70, 20, 71, 21))
        self.RB_A.setObjectName("RB_A")
        self.RB_B = QtWidgets.QRadioButton(self.groupBox_2)
        self.RB_B.setGeometry(QtCore.QRect(70, 50, 81, 19))
        self.RB_B.setObjectName("RB_B")
        self.L_table_2 = QtWidgets.QLabel(self.groupBox_2)
        self.L_table_2.setGeometry(QtCore.QRect(10, 150, 371, 16))
        self.L_table_2.setObjectName("L_table_2")
        self.L_answer = QtWidgets.QLabel(self.groupBox_2)
        self.L_answer.setGeometry(QtCore.QRect(80, 150, 321, 16))
        self.L_answer.setText("")
        self.L_answer.setObjectName("L_answer")
        self.RB_C = QtWidgets.QRadioButton(self.groupBox_2)
        self.RB_C.setGeometry(QtCore.QRect(70, 80, 81, 19))
        self.RB_C.setObjectName("RB_C")
        self.RB_D = QtWidgets.QRadioButton(self.groupBox_2)
        self.RB_D.setGeometry(QtCore.QRect(70, 110, 81, 21))
        self.RB_D.setObjectName("RB_D")
        self.label_A = QtWidgets.QLabel(self.groupBox_2)
        self.label_A.setGeometry(QtCore.QRect(110, 20, 641, 21))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.label_A.setFont(font)
        self.label_A.setObjectName("label_A")
        self.label_B = QtWidgets.QLabel(self.groupBox_2)
        self.label_B.setGeometry(QtCore.QRect(110, 50, 641, 21))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_B.setFont(font)
        self.label_B.setObjectName("label_B")
        self.label_C = QtWidgets.QLabel(self.groupBox_2)
        self.label_C.setGeometry(QtCore.QRect(110, 80, 641, 21))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_C.setFont(font)
        self.label_C.setObjectName("label_C")
        self.label_D = QtWidgets.QLabel(self.groupBox_2)
        self.label_D.setGeometry(QtCore.QRect(110, 110, 641, 21))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_D.setFont(font)
        self.label_D.setObjectName("label_D")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(340, 20, 771, 261))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 751, 231))
        self.textEdit.setObjectName("textEdit")
        self.groupBox_5 = QtWidgets.QGroupBox(Form)
        self.groupBox_5.setGeometry(QtCore.QRect(340, 460, 771, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.B_next = QtWidgets.QPushButton(self.groupBox_5)
        self.B_next.setEnabled(True)
        self.B_next.setGeometry(QtCore.QRect(350, 30, 93, 28))
        self.B_next.setObjectName("B_next")
        self.B_rm = QtWidgets.QPushButton(self.groupBox_5)
        self.B_rm.setGeometry(QtCore.QRect(490, 30, 93, 28))
        self.B_rm.setObjectName("B_rm")
        self.B_answer = QtWidgets.QPushButton(self.groupBox_5)
        self.B_answer.setEnabled(True)
        self.B_answer.setGeometry(QtCore.QRect(70, 30, 93, 28))
        self.B_answer.setObjectName("B_answer")
        self.B_last = QtWidgets.QPushButton(self.groupBox_5)
        self.B_last.setEnabled(True)
        self.B_last.setGeometry(QtCore.QRect(210, 30, 93, 28))
        self.B_last.setObjectName("B_last")
        self.B_return = QtWidgets.QPushButton(self.groupBox_5)
        self.B_return.setGeometry(QtCore.QRect(630, 30, 93, 28))
        self.B_return.setObjectName("B_return")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 280, 321, 271))
        self.groupBox.setObjectName("groupBox")
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 301, 241))
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_4.setTitle(_translate("Form", "题量"))
        self.label.setText(_translate("Form", "总做题数："))
        self.label_3.setText(_translate("Form", "错题数："))
        self.label_5.setText(_translate("Form", "已复习："))
        self.label_6.setText(_translate("Form", "错误率："))
        self.groupBox_2.setTitle(_translate("Form", "选项"))
        self.RB_A.setText(_translate("Form", "A."))
        self.RB_B.setText(_translate("Form", "B."))
        self.L_table_2.setText(_translate("Form", "正确答案："))
        self.RB_C.setText(_translate("Form", "C."))
        self.RB_D.setText(_translate("Form", "D."))
        self.label_A.setText(_translate("Form", "TextLabel"))
        self.label_B.setText(_translate("Form", "TextLabel"))
        self.label_C.setText(_translate("Form", "TextLabel"))
        self.label_D.setText(_translate("Form", "TextLabel"))
        self.groupBox_3.setTitle(_translate("Form", "题目"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>"))
        self.groupBox_5.setTitle(_translate("Form", "功能"))
        self.B_next.setText(_translate("Form", "下一题"))
        self.B_rm.setText(_translate("Form", "从错题删除"))
        self.B_answer.setText(_translate("Form", "查看答案"))
        self.B_last.setText(_translate("Form", "上一题"))
        self.B_return.setText(_translate("Form", "返回"))
        self.groupBox.setTitle(_translate("Form", "GroupBox"))
