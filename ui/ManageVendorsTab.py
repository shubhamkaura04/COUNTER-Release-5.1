# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ManageVendorsTab.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_manage_vendor_tab(object):
    def setupUi(self, manage_vendor_tab):
        manage_vendor_tab.setObjectName("manage_vendor_tab")
        manage_vendor_tab.resize(932, 494)
        manage_vendor_tab.setStyleSheet("*{\n"
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
"#manage_vendor_tab{\n"
"background-color:#1f232a;\n"
"}\n"
"#EditVendor{\n"
"background-color:#16191d;\n"
"}\n"
"QPushButton{\n"
"text-align:left;\n"
"padding: 5px 10px;\n"
"\n"
"border-top-left-radius:5px;\n"
"border-bottom-left-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:grey;\n"
"text-align:left;\n"
"padding:2px 10px;\n"
"color:white;}")
        self.gridLayout_2 = QtWidgets.QGridLayout(manage_vendor_tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.centralwidget = QtWidgets.QWidget(manage_vendor_tab)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.SelectVendor = QtWidgets.QWidget(self.centralwidget)
        self.SelectVendor.setObjectName("SelectVendor")
        self.gridLayout = QtWidgets.QGridLayout(self.SelectVendor)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.SelectVendor)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 1, 1, 1)
        self.vendorsListView = QtWidgets.QListView(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.vendorsListView.setFont(font)
        self.vendorsListView.setStyleSheet("QListView {\n"
"    background-color: #cccccc;\n"
"\n"
"    color:black;\n"
"}\n"
"\n"
"#vendorsListView{\n"
"\n"
"\n"
"    border: 5px solid #000000;\n"
"    border-color: rgb(166, 166, 166);\n"
"color:black;\n"
"\n"
"\n"
"}")
        self.vendorsListView.setAlternatingRowColors(True)
        self.vendorsListView.setObjectName("vendorsListView")
        self.gridLayout_3.addWidget(self.vendorsListView, 2, 0, 1, 1)
        self.vendorsListView_2 = QtWidgets.QListView(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.vendorsListView_2.setFont(font)
        self.vendorsListView_2.setStyleSheet("QListView {\n"
"    background-color: #cccccc;\n"
"\n"
"color:black;\n"
"}\n"
"\n"
"#vendorsListView{\n"
"color:black;\n"
"\n"
"    border: 5px solid #000000;\n"
"    border-color: rgb(166, 166, 166);\n"
"\n"
"\n"
"}")
        self.vendorsListView_2.setAlternatingRowColors(True)
        self.vendorsListView_2.setObjectName("vendorsListView_2")
        self.gridLayout_3.addWidget(self.vendorsListView_2, 2, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("QPushButton {\n"
"    border: 2px solid #000000;\n"
"border-color:grey;\n"
"border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: lightblue;\n"
"}\n"
"\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addVendorButton = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addVendorButton.sizePolicy().hasHeightForWidth())
        self.addVendorButton.setSizePolicy(sizePolicy)
        self.addVendorButton.setStyleSheet("text-align: center;\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/Icons/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addVendorButton.setIcon(icon)
        self.addVendorButton.setObjectName("addVendorButton")
        self.horizontalLayout.addWidget(self.addVendorButton)
        self.importVendorsButton = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.importVendorsButton.sizePolicy().hasHeightForWidth())
        self.importVendorsButton.setSizePolicy(sizePolicy)
        self.importVendorsButton.setStyleSheet("text-align: center;\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/Icons/import.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.importVendorsButton.setIcon(icon1)
        self.importVendorsButton.setObjectName("importVendorsButton")
        self.horizontalLayout.addWidget(self.importVendorsButton)
        self.exportVendorsButton = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exportVendorsButton.sizePolicy().hasHeightForWidth())
        self.exportVendorsButton.setSizePolicy(sizePolicy)
        self.exportVendorsButton.setStyleSheet("text-align: center;\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/Icons/export - Copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exportVendorsButton.setIcon(icon2)
        self.exportVendorsButton.setObjectName("exportVendorsButton")
        self.horizontalLayout.addWidget(self.exportVendorsButton)
        self.editvendorsbutton = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editvendorsbutton.sizePolicy().hasHeightForWidth())
        self.editvendorsbutton.setSizePolicy(sizePolicy)
        self.editvendorsbutton.setStyleSheet("text-align: center;\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resources/Icons/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editvendorsbutton.setIcon(icon3)
        self.editvendorsbutton.setObjectName("editvendorsbutton")
        self.horizontalLayout.addWidget(self.editvendorsbutton)
        self.gridLayout_3.addWidget(self.frame_2, 3, 0, 1, 2)
        self.label_13 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("")
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.SelectVendor, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.centralwidget, 0, 0, 1, 1)

        self.retranslateUi(manage_vendor_tab)
        QtCore.QMetaObject.connectSlotsByName(manage_vendor_tab)

    def retranslateUi(self, manage_vendor_tab):
        _translate = QtCore.QCoreApplication.translate
        manage_vendor_tab.setWindowTitle(_translate("manage_vendor_tab", "MainWindow"))
        self.label.setText(_translate("manage_vendor_tab", "5.1"))
        self.label_2.setText(_translate("manage_vendor_tab", "5.0"))
        self.addVendorButton.setText(_translate("manage_vendor_tab", "Add New Vendor"))
        self.importVendorsButton.setText(_translate("manage_vendor_tab", "Import Vendors"))
        self.exportVendorsButton.setToolTip(_translate("manage_vendor_tab", "<html><head/><body><p><img src=\":/newPrefix/save_icon.png\"/>yguhbnj</p></body></html>"))
        self.exportVendorsButton.setText(_translate("manage_vendor_tab", "Export Vendors"))
        self.editvendorsbutton.setText(_translate("manage_vendor_tab", "Edit Vendor"))
        self.label_13.setText(_translate("manage_vendor_tab", "<html><head/><body><p align=\"center\">Select Vendor</p></body></html>"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    manage_vendor_tab = QtWidgets.QWidget()
    ui = Ui_manage_vendor_tab()
    ui.setupUi(manage_vendor_tab)
    manage_vendor_tab.show()
    sys.exit(app.exec_())
