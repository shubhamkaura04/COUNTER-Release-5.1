# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddVendor51.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addVendor51Dialog(object):
    def setupUi(self, addVendor51Dialog):
        addVendor51Dialog.setObjectName("addVendor51Dialog")
        addVendor51Dialog.resize(957, 641)
        addVendor51Dialog.setStyleSheet("*{\n"
"    \n"
"border:none;\n"
"background-color:transparent;\n"
"background:none;\n"
"padding:0;\n"
"margin:0;\n"
"color:#fff;\n"
"}\n"
"\n"
"\n"
"\n"
"#centralwidget{\n"
"background-color:#1f232a;\n"
"}\n"
"\n"
"QPushButton{\n"
"text-align:left;\n"
"padding: 5px 10px;\n"
"\n"
"border-top-left-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:grey;\n"
"text-align:left;\n"
"padding:2px 10px;\n"
"color:white;}")
        self.centralwidget = QtWidgets.QWidget(addVendor51Dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("#frame{border:2px solid grey; border-radius:15px;}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"\n"
"QLineEdit {\n"
"    background-color: #cccccc;\n"
"    border-radius: 20px; \n"
"\n"
"}\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("text-align:centre;")
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 1, 1, 2)
        self.AddNewVendor = QtWidgets.QFrame(self.frame_3)
        self.AddNewVendor.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(8)
        self.AddNewVendor.setFont(font)
        self.AddNewVendor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AddNewVendor.setObjectName("AddNewVendor")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.AddNewVendor)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_28 = QtWidgets.QLabel(self.AddNewVendor)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.gridLayout_5.addWidget(self.label_28, 14, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.AddNewVendor)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 9, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.AddNewVendor)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 5, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.AddNewVendor)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 6, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.AddNewVendor)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.AddNewVendor)
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 6, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.AddNewVendor)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 7, 0, 1, 1)
        self.versionEdit = QtWidgets.QLabel(self.AddNewVendor)
        self.versionEdit.setObjectName("versionEdit")
        self.gridLayout_5.addWidget(self.versionEdit, 0, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.AddNewVendor)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 1, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.AddNewVendor)
        self.label_18.setObjectName("label_18")
        self.gridLayout_5.addWidget(self.label_18, 3, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.AddNewVendor)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 11, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.AddNewVendor)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 8, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.AddNewVendor)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 5, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.AddNewVendor)
        self.label_15.setObjectName("label_15")
        self.gridLayout_5.addWidget(self.label_15, 0, 0, 1, 1)
        self.provider = QtWidgets.QLabel(self.AddNewVendor)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.provider.setFont(font)
        self.provider.setObjectName("provider")
        self.gridLayout_5.addWidget(self.provider, 13, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.AddNewVendor)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.AddNewVendor)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 10, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.AddNewVendor)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 12, 0, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(self.AddNewVendor)
        self.nameEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.nameEdit.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #808080;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"    color: white;\n"
"    background-color: #2E2F30;\n"
"}\n"
"\n"
"")
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout_5.addWidget(self.nameEdit, 1, 2, 1, 1)
        self.name_validation_label = QtWidgets.QLabel(self.AddNewVendor)
        self.name_validation_label.setText("")
        self.name_validation_label.setObjectName("name_validation_label")
        self.gridLayout_5.addWidget(self.name_validation_label, 2, 2, 1, 1)
        self.baseUrlEdit = QtWidgets.QLineEdit(self.AddNewVendor)
        self.baseUrlEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.baseUrlEdit.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #808080;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"    color: white;\n"
"background-color: #2E2F30;\n"
"}\n"
"\n"
"")
        self.baseUrlEdit.setObjectName("baseUrlEdit")
        self.gridLayout_5.addWidget(self.baseUrlEdit, 3, 2, 1, 1)
        self.url_validation_label = QtWidgets.QLabel(self.AddNewVendor)
        self.url_validation_label.setText("")
        self.url_validation_label.setObjectName("url_validation_label")
        self.gridLayout_5.addWidget(self.url_validation_label, 4, 2, 1, 1)
        self.All_reports_edit_fetch = QtWidgets.QDateEdit(self.AddNewVendor)
        self.All_reports_edit_fetch.setEnabled(True)
        self.All_reports_edit_fetch.setMinimumSize(QtCore.QSize(64, 30))
        self.All_reports_edit_fetch.setMaximumSize(QtCore.QSize(65, 16777215))
        self.All_reports_edit_fetch.setStyleSheet("QDateEdit {\n"
"    border: 2px solid #808080;\n"
"background-color: #2E2F30;\n"
"    border-radius: 4px;\n"
"    padding-left: 5px;\n"
"min-width: 62px;\n"
"    max-width: 62px;\n"
"}\n"
"\n"
"QDateEdit::up-button, QDateEdit::down-button {\n"
"    border: none;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QDateEdit::up-button {\n"
"    subcontrol-position: top right;\n"
"}\n"
"\n"
"QDateEdit::down-button {\n"
"    subcontrol-position: bottom right;\n"
"}\n"
"\n"
"QDateEdit::up-arrow, QDateEdit::down-arrow {\n"
"    border: 5px solid rgba(255, 255, 255, 0);\n"
"    width: 0;\n"
"    height: 0;\n"
"}\n"
"\n"
"QDateEdit::up-arrow {\n"
"    border-top: none;\n"
"    border-bottom-color: white;\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"    border-bottom: none;\n"
"    border-top-color: white;\n"
"}")
        self.All_reports_edit_fetch.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 12, 25), QtCore.QTime(0, 0, 0)))
        self.All_reports_edit_fetch.setObjectName("All_reports_edit_fetch")
        self.gridLayout_5.addWidget(self.All_reports_edit_fetch, 5, 2, 1, 1)
        self.customerIdEdit = QtWidgets.QLineEdit(self.AddNewVendor)
        self.customerIdEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.customerIdEdit.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #808080;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"    color: white;\n"
"background-color: #2E2F30;\n"
"}\n"
"\n"
"")
        self.customerIdEdit.setObjectName("customerIdEdit")
        self.gridLayout_5.addWidget(self.customerIdEdit, 6, 2, 1, 1)
        self.requestorIdEdit = QtWidgets.QLineEdit(self.AddNewVendor)
        self.requestorIdEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.requestorIdEdit.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #808080;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"background-color: #2E2F30;\n"
"    color: white;\n"
"}\n"
"\n"
"")
        self.requestorIdEdit.setObjectName("requestorIdEdit")
        self.gridLayout_5.addWidget(self.requestorIdEdit, 7, 2, 1, 1)
        self.platformEdit = QtWidgets.QLineEdit(self.AddNewVendor)
        self.platformEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.platformEdit.setStyleSheet("QLineEdit {\n"
"background-color: #2E2F30;\n"
"    border: 2px solid #808080;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"")
        self.platformEdit.setObjectName("platformEdit")
        self.gridLayout_5.addWidget(self.platformEdit, 8, 2, 1, 1)
        self.apiKeyEdit = QtWidgets.QLineEdit(self.AddNewVendor)
        self.apiKeyEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.apiKeyEdit.setStyleSheet("QLineEdit {\n"
"background-color: #2E2F30;\n"
"    border: 2px solid #808080;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"")
        self.apiKeyEdit.setObjectName("apiKeyEdit")
        self.gridLayout_5.addWidget(self.apiKeyEdit, 9, 2, 1, 1)
        self.two_attempts_check_box = QtWidgets.QCheckBox(self.AddNewVendor)
        self.two_attempts_check_box.setText("")
        self.two_attempts_check_box.setObjectName("two_attempts_check_box")
        self.gridLayout_5.addWidget(self.two_attempts_check_box, 10, 2, 1, 1)
        self.ip_checking_check_box = QtWidgets.QCheckBox(self.AddNewVendor)
        self.ip_checking_check_box.setText("")
        self.ip_checking_check_box.setObjectName("ip_checking_check_box")
        self.gridLayout_5.addWidget(self.ip_checking_check_box, 11, 2, 1, 1)
        self.requests_throttled_check_box = QtWidgets.QCheckBox(self.AddNewVendor)
        self.requests_throttled_check_box.setText("")
        self.requests_throttled_check_box.setObjectName("requests_throttled_check_box")
        self.gridLayout_5.addWidget(self.requests_throttled_check_box, 12, 2, 1, 1)
        self.providerEdit = QtWidgets.QLineEdit(self.AddNewVendor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.providerEdit.sizePolicy().hasHeightForWidth())
        self.providerEdit.setSizePolicy(sizePolicy)
        self.providerEdit.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #808080;\n"
"    border-radius: 4px;\n"
"background-color: #2E2F30;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"")
        self.providerEdit.setObjectName("providerEdit")
        self.gridLayout_5.addWidget(self.providerEdit, 13, 2, 1, 1)
        self.notesEdit = QtWidgets.QLineEdit(self.AddNewVendor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notesEdit.sizePolicy().hasHeightForWidth())
        self.notesEdit.setSizePolicy(sizePolicy)
        self.notesEdit.setMinimumSize(QtCore.QSize(339, 0))
        self.notesEdit.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #808080;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"    color: white;\n"
"background-color: #2E2F30;\n"
"}\n"
"\n"
"")
        self.notesEdit.setObjectName("notesEdit")
        self.gridLayout_5.addWidget(self.notesEdit, 14, 2, 1, 1)
        self.gridLayout_2.addWidget(self.AddNewVendor, 1, 0, 1, 3)
        self.validate_button = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.validate_button.setFont(font)
        self.validate_button.setStyleSheet("QPushButton {\n"
"    background-color: #1768E3; \n"
"    color: #FFFFFF;\n"
"    font: bold;\n"
"   border-radius: 4px;\n"
"text-align: center;\n"
"}\n"
"\n"
"")
        self.validate_button.setObjectName("validate_button")
        self.gridLayout_2.addWidget(self.validate_button, 3, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.buttonBox.setFont(font)
        self.buttonBox.setStyleSheet("border: 2px solid grey;\n"
"border-radius: 8px;\n"
"background-color: #000000;\n"
"")
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 2, 2, 2, 1)
        self.verticalLayout.addWidget(self.frame_3)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 2)
        addVendor51Dialog.setCentralWidget(self.centralwidget)

        self.retranslateUi(addVendor51Dialog)
        QtCore.QMetaObject.connectSlotsByName(addVendor51Dialog)

    def retranslateUi(self, addVendor51Dialog):
        _translate = QtCore.QCoreApplication.translate
        addVendor51Dialog.setWindowTitle(_translate("addVendor51Dialog", "MainWindow"))
        self.label_7.setText(_translate("addVendor51Dialog", "<html><head/><body><p align=\"center\">Add New Vendor</p></body></html>"))
        self.label_28.setText(_translate("addVendor51Dialog", "Notes"))
        self.label_5.setText(_translate("addVendor51Dialog", "API Key"))
        self.label_13.setText(_translate("addVendor51Dialog", "*"))
        self.label_3.setText(_translate("addVendor51Dialog", "Customer ID"))
        self.label_2.setText(_translate("addVendor51Dialog", "Base URL"))
        self.label_14.setText(_translate("addVendor51Dialog", "*"))
        self.label_4.setText(_translate("addVendor51Dialog", "Requester ID"))
        self.versionEdit.setText(_translate("addVendor51Dialog", "5.1"))
        self.label_12.setText(_translate("addVendor51Dialog", "*"))
        self.label_18.setText(_translate("addVendor51Dialog", "*"))
        self.label_9.setText(_translate("addVendor51Dialog", "IP Checking required"))
        self.label_6.setText(_translate("addVendor51Dialog", "Platform"))
        self.label_10.setText(_translate("addVendor51Dialog", "Starting Year"))
        self.label_15.setText(_translate("addVendor51Dialog", "Version"))
        self.provider.setText(_translate("addVendor51Dialog", "Provider"))
        self.label.setText(_translate("addVendor51Dialog", "Name"))
        self.label_8.setText(_translate("addVendor51Dialog", "2 Attempts needed"))
        self.label_11.setText(_translate("addVendor51Dialog", "Request throttled"))
        self.All_reports_edit_fetch.setDisplayFormat(_translate("addVendor51Dialog", "yyyy"))
        self.validate_button.setText(_translate("addVendor51Dialog", "Validate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addVendor51Dialog = QtWidgets.QMainWindow()
    ui = Ui_addVendor51Dialog()
    ui.setupUi(addVendor51Dialog)
    addVendor51Dialog.show()
    sys.exit(app.exec_())
