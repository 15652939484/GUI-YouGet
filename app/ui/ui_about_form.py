# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutform.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutForm(object):
    def setupUi(self, AboutForm):
        AboutForm.setObjectName("AboutForm")
        AboutForm.resize(500, 270)
        self.label_logo = QtWidgets.QLabel(AboutForm)
        self.label_logo.setGeometry(QtCore.QRect(20, 100, 131, 121))
        self.label_logo.setStyleSheet("image: url(:/res/favicon.ico);")
        self.label_logo.setText("")
        self.label_logo.setObjectName("label_logo")
        self.label_info = QtWidgets.QLabel(AboutForm)
        self.label_info.setGeometry(QtCore.QRect(170, 80, 301, 161))
        self.label_info.setObjectName("label_info")
        self.label_title = QtWidgets.QLabel(AboutForm)
        self.label_title.setGeometry(QtCore.QRect(180, 20, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")

        self.retranslateUi(AboutForm)
        QtCore.QMetaObject.connectSlotsByName(AboutForm)

    def retranslateUi(self, AboutForm):
        _translate = QtCore.QCoreApplication.translate
        AboutForm.setWindowTitle(_translate("AboutForm", "About"))
        self.label_info.setText(_translate("AboutForm", "<html><head/><body><p><a href=\"http://www.ingbyr.tk/2016/05/16/youget/\"><span style=\" font-size:11pt; text-decoration: underline; color:#0000ff;\">GUI-YouGet</span></a><span style=\" font-size:11pt;\"> is a video download software </span></p><p><span style=\" font-size:11pt;\">Version + version + | License </span><a href=\"https://raw.githubusercontent.com/ingbyr/GUI-YouGet/master/LICENSE.txt\"><span style=\" font-size:11pt; text-decoration: underline; color:#0000ff;\">MIT</span></a><span style=\" font-size:11pt;\"><br/><br/>Based on the program </span><a href=\"https://github.com/soimort/you-get\"><span style=\" font-size:11pt; text-decoration: underline; color:#0000ff;\">you-get</span></a><span style=\" font-size:11pt;\"><br/></span></p><p><span style=\" font-size:11pt;\">Coder: InG_byr ( </span><a href=\"http://www.ingbyr.tk\"><span style=\" font-size:11pt; text-decoration: underline; color:#0000ff;\">Blog</span></a><a href=\"http://www.weibo.com/zwkv5\"><span style=\" font-size:11pt; text-decoration: underline; color:#0000ff;\">Sina Weibo</span></a><span style=\" font-size:11pt;\"> )</span></p></body></html>"))
        self.label_title.setText(_translate("AboutForm", "GUI-YouGet"))

