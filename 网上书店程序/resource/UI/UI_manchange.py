# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_manchange.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Manchange(object):
    def setupUi(self, Manchange):
        Manchange.setObjectName("Manchange")
        Manchange.resize(918, 761)
        Manchange.setStyleSheet("QPushButton:hover{\n"
"        color:red\n"
"        }\n"
"QLineEdit{\n"
"        border:1px solid gray;;\n"
"        border-radius:10px;\n"
"        padding:2px 4px;\n"
"}\n"
"QWidget{\n"
"        color:#0c0a0a;\n"
"        background:rgb(255, 255, 253);\n"
"        border-top:1px solid darkGray;\n"
"        border-bottom:1px solid darkGray;\n"
"        border-right:1px solid darkGray;\n"
"        border-left:1px solid darkGray;\n"
"        border-top-left-radius:10px;\n"
"        border-top-right-radius:10px;\n"
"        border-bottom-right-radius:10px;\n"
"        border-bottom-left-radius:10px;\n"
"    }\n"
"QLabel{\n"
"        border:none;}\n"
"\n"
"")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Manchange)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem1)
        self.titlelabel = QtWidgets.QLabel(Manchange)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(22)
        self.titlelabel.setFont(font)
        self.titlelabel.setObjectName("titlelabel")
        self.horizontalLayout_13.addWidget(self.titlelabel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.label = QtWidgets.QLabel(Manchange)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.phone_2 = QtWidgets.QLabel(Manchange)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.phone_2.setFont(font)
        self.phone_2.setObjectName("phone_2")
        self.horizontalLayout_4.addWidget(self.phone_2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.textBrowser_id = QtWidgets.QTextBrowser(Manchange)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_id.sizePolicy().hasHeightForWidth())
        self.textBrowser_id.setSizePolicy(sizePolicy)
        self.textBrowser_id.setMinimumSize(QtCore.QSize(400, 40))
        self.textBrowser_id.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textBrowser_id.setFont(font)
        self.textBrowser_id.setObjectName("textBrowser_id")
        self.horizontalLayout_4.addWidget(self.textBrowser_id)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem11)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem12)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem13)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem14)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem15)
        self.phone = QtWidgets.QLabel(Manchange)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.phone.setFont(font)
        self.phone.setObjectName("phone")
        self.horizontalLayout_2.addWidget(self.phone)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem16)
        self.textEdit_mph = QtWidgets.QTextEdit(Manchange)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_mph.sizePolicy().hasHeightForWidth())
        self.textEdit_mph.setSizePolicy(sizePolicy)
        self.textEdit_mph.setMinimumSize(QtCore.QSize(400, 40))
        self.textEdit_mph.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit_mph.setFont(font)
        self.textEdit_mph.setObjectName("textEdit_mph")
        self.horizontalLayout_2.addWidget(self.textEdit_mph)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem17)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem18)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem19)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem20)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem21)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem22)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem23)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem24)
        self.id = QtWidgets.QLabel(Manchange)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.id.setFont(font)
        self.id.setObjectName("id")
        self.horizontalLayout_3.addWidget(self.id)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem25)
        self.textEdit_mpnm = QtWidgets.QTextEdit(Manchange)
        self.textEdit_mpnm.setMinimumSize(QtCore.QSize(400, 40))
        self.textEdit_mpnm.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit_mpnm.setFont(font)
        self.textEdit_mpnm.setObjectName("textEdit_mpnm")
        self.horizontalLayout_3.addWidget(self.textEdit_mpnm)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem26)
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem27)
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem28)
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem29)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem30 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem30)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem31)
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem32)
        spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem33)
        self.key = QtWidgets.QLabel(Manchange)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.key.setFont(font)
        self.key.setObjectName("key")
        self.horizontalLayout.addWidget(self.key)
        spacerItem34 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem34)
        self.textEdit_mpsw = QtWidgets.QTextEdit(Manchange)
        self.textEdit_mpsw.setMinimumSize(QtCore.QSize(400, 40))
        self.textEdit_mpsw.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit_mpsw.setFont(font)
        self.textEdit_mpsw.setObjectName("textEdit_mpsw")
        self.horizontalLayout.addWidget(self.textEdit_mpsw)
        spacerItem35 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem35)
        spacerItem36 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem36)
        spacerItem37 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem37)
        spacerItem38 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem38)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem39 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem39)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem40 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem40)
        spacerItem41 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem41)
        spacerItem42 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem42)
        self.e_mail = QtWidgets.QLabel(Manchange)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.e_mail.setFont(font)
        self.e_mail.setObjectName("e_mail")
        self.horizontalLayout_5.addWidget(self.e_mail)
        spacerItem43 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem43)
        self.textEdit_mpem = QtWidgets.QTextEdit(Manchange)
        self.textEdit_mpem.setMinimumSize(QtCore.QSize(400, 40))
        self.textEdit_mpem.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit_mpem.setFont(font)
        self.textEdit_mpem.setObjectName("textEdit_mpem")
        self.horizontalLayout_5.addWidget(self.textEdit_mpem)
        spacerItem44 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem44)
        spacerItem45 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem45)
        spacerItem46 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem46)
        spacerItem47 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem47)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        spacerItem48 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem48)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem49 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem49)
        self.confirmBu = QtWidgets.QPushButton(Manchange)
        self.confirmBu.setMinimumSize(QtCore.QSize(120, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.confirmBu.setFont(font)
        self.confirmBu.setObjectName("confirmBu")
        self.horizontalLayout_8.addWidget(self.confirmBu)
        spacerItem50 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem50)
        spacerItem51 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem51)
        self.pushButton = QtWidgets.QPushButton(Manchange)
        self.pushButton.setMinimumSize(QtCore.QSize(120, 50))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_8.addWidget(self.pushButton)
        spacerItem52 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem52)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Manchange)
        self.pushButton.clicked.connect(Manchange.close)
        QtCore.QMetaObject.connectSlotsByName(Manchange)

    def retranslateUi(self, Manchange):
        _translate = QtCore.QCoreApplication.translate
        Manchange.setWindowTitle(_translate("Manchange", "Dialog"))
        self.titlelabel.setText(_translate("Manchange", "管理员信息修改"))
        self.label.setText(_translate("Manchange", "                                         [注]：带*为必填项,带#项不可修改"))
        self.phone_2.setText(_translate("Manchange", "#ID号："))
        self.phone.setText(_translate("Manchange", "电话："))
        self.id.setText(_translate("Manchange", "*账号："))
        self.key.setText(_translate("Manchange", "*密码："))
        self.e_mail.setText(_translate("Manchange", "邮箱："))
        self.confirmBu.setText(_translate("Manchange", "确认修改"))
        self.pushButton.setText(_translate("Manchange", "退出"))
