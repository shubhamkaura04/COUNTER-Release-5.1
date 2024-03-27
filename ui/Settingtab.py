# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Settingtab.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingTab(object):
    def setupUi(self, SettingTab):
        SettingTab.setObjectName("SettingTab")
        SettingTab.resize(611, 580)
        SettingTab.setStyleSheet("*{\n"
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
"#SettingTab{\n"
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
"border-botton-left-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:grey;\n"
"text-align:left;\n"
"padding:2px 10px;\n"
"color:white;}")
        self.gridLayout_5 = QtWidgets.QGridLayout(SettingTab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.centralwidget = QtWidgets.QWidget(SettingTab)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(-1)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("font-size: 16px;")
        self.label.setObjectName("label")
        self.gridLayout_7.addWidget(self.label, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(-1)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("font-size: 15px;")
        self.label_9.setObjectName("label_9")
        self.gridLayout_7.addWidget(self.label_9, 6, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("QFrame{\n"
"    border: 2px solid #000000;\n"
"border-color:grey;\n"
"border-radius:15px;\n"
"padding: 10px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.select_directory_button = QtWidgets.QPushButton(self.frame_2)
        self.select_directory_button.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.select_directory_button.setFont(font)
        self.select_directory_button.setStyleSheet("QPushButton {\n"
"    background-color: #1768E3; \n"
"    color: #FFFFFF;\n"
"    font: bold;\n"
"   border-radius: 4px;\n"
"text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: #2095E6;\n"
"}\n"
"\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Final Project/COUNTER-Release-5.1/ui/resources/Icons/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.select_directory_button.setIcon(icon)
        self.select_directory_button.setObjectName("select_directory_button")
        self.gridLayout.addWidget(self.select_directory_button, 0, 4, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.directory_type_comboBox = QtWidgets.QComboBox(self.frame_2)
        self.directory_type_comboBox.setEnabled(True)
        self.directory_type_comboBox.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(-1)
        self.directory_type_comboBox.setFont(font)
        self.directory_type_comboBox.setStyleSheet("\n"
"QComboBox {\n"
"    color: white; \n"
"    background-color: #2E2F30;\n"
"border-radius: 4px;\n"
"padding: 4px;\n"
"font-size: 13px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: white; \n"
"    background-color: #2E2F30;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"")
        self.directory_type_comboBox.setEditable(False)
        self.directory_type_comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.directory_type_comboBox.setMinimumContentsLength(15)
        self.directory_type_comboBox.setObjectName("directory_type_comboBox")
        self.directory_type_comboBox.addItem("")
        self.directory_type_comboBox.addItem("")
        self.directory_type_comboBox.addItem("")
        self.directory_type_comboBox.addItem("")
        self.gridLayout.addWidget(self.directory_type_comboBox, 0, 1, 1, 2)
        self.request_interval_spin_box = QtWidgets.QSpinBox(self.frame_2)
        self.request_interval_spin_box.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(-1)
        self.request_interval_spin_box.setFont(font)
        self.request_interval_spin_box.setStyleSheet("QSpinBox {\n"
"background-color: #2E2F30;\n"
"    border: 2px solid #808080;\n"
"    border-radius: 4px;\n"
"    padding-left: 5px;\n"
"    padding: 4px;\n"
"font-size: 14px;\n"
"padding-left: 6px;\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    border: none;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-position: top right;\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-position: bottom right;\n"
"}\n"
"\n"
"QSpinBox::up-arrow, QSpinBox::down-arrow {\n"
"    border: 5px solid rgba(255, 255, 255, 0);\n"
"    width: 0;\n"
"    height: 0;\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    border-top: none;\n"
"    border-bottom-color: white;\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    border-bottom: none;\n"
"    border-top-color: white;\n"
"}")
        self.request_interval_spin_box.setMaximum(9999)
        self.request_interval_spin_box.setObjectName("request_interval_spin_box")
        self.gridLayout.addWidget(self.request_interval_spin_box, 1, 1, 1, 3)
        self.user_agent_edit = QtWidgets.QLineEdit(self.frame_2)
        self.user_agent_edit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(-1)
        self.user_agent_edit.setFont(font)
        self.user_agent_edit.setStyleSheet("QLineEdit {\n"
"background-color: #2E2F30;\n"
"    border: 2px solid #808080;\n"
"    border-radius: 4px;\n"
"    padding-left: 5px;\n"
"    padding: 4px;\n"
"font-size: 14px;\n"
"padding-left: 6px;\n"
"}")
        self.user_agent_edit.setObjectName("user_agent_edit")
        self.gridLayout.addWidget(self.user_agent_edit, 3, 1, 1, 3)
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(-1)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("Border:none;\n"
"font-size: 13px;")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.request_timeout_spin_box = QtWidgets.QSpinBox(self.frame_2)
        self.request_timeout_spin_box.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(-1)
        self.request_timeout_spin_box.setFont(font)
        self.request_timeout_spin_box.setStyleSheet("QSpinBox {\n"
"background-color: #2E2F30;\n"
"    border: 2px solid #808080;\n"
"    border-radius: 4px;\n"
"    padding-left: 5px;\n"
"    padding: 4px;\n"
"font-size: 14px;\n"
"padding-left: 6px;\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    border: none;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-position: top right;\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-position: bottom right;\n"
"}\n"
"\n"
"QSpinBox::up-arrow, QSpinBox::down-arrow {\n"
"    border: 5px solid rgba(255, 255, 255, 0);\n"
"    width: 0;\n"
"    height: 0;\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    border-top: none;\n"
"    border-bottom-color: white;\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    border-bottom: none;\n"
"    border-top-color: white;\n"
"}")
        self.request_timeout_spin_box.setMaximum(9999)
        self.request_timeout_spin_box.setObjectName("request_timeout_spin_box")
        self.gridLayout.addWidget(self.request_timeout_spin_box, 2, 1, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(-1)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("Border:none;\n"
"font-size: 13px;")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.directory_edit = QtWidgets.QLineEdit(self.frame_2)
        self.directory_edit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(-1)
        self.directory_edit.setFont(font)
        self.directory_edit.setStyleSheet("QLineEdit {\n"
"    color: white; \n"
"    background-color: #2E2F30;\n"
"    padding: 4px;\n"
"font-size: 13px;\n"
"padding-left: 6px;\n"
"}\n"
"")
        self.directory_edit.setObjectName("directory_edit")
        self.gridLayout.addWidget(self.directory_edit, 0, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(-1)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("Border:none;\n"
"font-size: 13px;")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(-1)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("Border:none;\n"
"font-size: 13px;")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frame_2, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem1, 10, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem2, 5, 0, 1, 1)
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        self.save_button.setFont(font)
        self.save_button.setStyleSheet("QPushButton {\n"
"    background-color: #1768E3; \n"
"    color: #FFFFFF;\n"
"    font: bold;\n"
"   border-radius: 4px;\n"
"text-align: center;\n"
"    padding: 6px;\n"
"font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: #2095E6;\n"
"cursor: pointer;\n"
"}\n"
"\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Final Project/COUNTER-Release-5.1/ui/resources/Icons/diskette.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_button.setIcon(icon1)
        self.save_button.setIconSize(QtCore.QSize(25, 25))
        self.save_button.setObjectName("save_button")
        self.gridLayout_7.addWidget(self.save_button, 4, 0, 1, 1, QtCore.Qt.AlignRight)
        self.settings_rebuild_database_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        self.settings_rebuild_database_button.setFont(font)
        self.settings_rebuild_database_button.setStyleSheet("QPushButton {\n"
"    background-color: #1768E3; \n"
"    color: #FFFFFF;\n"
"    font: bold;\n"
"   border-radius: 4px;\n"
"text-align: center;\n"
"padding: 7px;\n"
"font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: #2095E6;\n"
"cursor: pointer;\n"
"}\n"
"\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Final Project/COUNTER-Release-5.1/ui/resources/Icons/database.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_rebuild_database_button.setIcon(icon2)
        self.settings_rebuild_database_button.setIconSize(QtCore.QSize(25, 25))
        self.settings_rebuild_database_button.setObjectName("settings_rebuild_database_button")
        self.gridLayout_7.addWidget(self.settings_rebuild_database_button, 9, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_5.addWidget(self.centralwidget, 0, 0, 1, 1)

        self.retranslateUi(SettingTab)
        QtCore.QMetaObject.connectSlotsByName(SettingTab)
        SettingTab.setTabOrder(self.directory_type_comboBox, self.directory_edit)
        SettingTab.setTabOrder(self.directory_edit, self.select_directory_button)
        SettingTab.setTabOrder(self.select_directory_button, self.request_interval_spin_box)
        SettingTab.setTabOrder(self.request_interval_spin_box, self.request_timeout_spin_box)
        SettingTab.setTabOrder(self.request_timeout_spin_box, self.user_agent_edit)
        SettingTab.setTabOrder(self.user_agent_edit, self.save_button)
        SettingTab.setTabOrder(self.save_button, self.settings_rebuild_database_button)

    def retranslateUi(self, SettingTab):
        _translate = QtCore.QCoreApplication.translate
        SettingTab.setWindowTitle(_translate("SettingTab", "MainWindow"))
        self.label.setText(_translate("SettingTab", "<html><head/><body><p align=\"center\">Settings</p></body></html>"))
        self.label_9.setText(_translate("SettingTab", "<html><head/><body><p align=\"center\">If Database gets Corrupted</p></body></html>"))
        self.select_directory_button.setText(_translate("SettingTab", "Choose"))
        self.directory_type_comboBox.setItemText(0, _translate("SettingTab", "Search database"))
        self.directory_type_comboBox.setItemText(1, _translate("SettingTab", "Vendor data file"))
        self.directory_type_comboBox.setItemText(2, _translate("SettingTab", "Yearly reports"))
        self.directory_type_comboBox.setItemText(3, _translate("SettingTab", "Other reports"))
        self.label_6.setToolTip(_translate("SettingTab", "How program identifies itself to the SUSHI servers. Some vendors will reject some particular user agents. Only change this if there is a known problem as it will affect all requests to all vendors. "))
        self.label_6.setText(_translate("SettingTab", "User agent"))
        self.label_2.setToolTip(_translate("SettingTab", "The number of seconds the program will wait between sending each report request to a given vendor."))
        self.label_2.setText(_translate("SettingTab", "Report request interval"))
        self.label_7.setToolTip(_translate("SettingTab", "We can set where to save search database, vendor data file and yearly reports here"))
        self.label_7.setText(_translate("SettingTab", "Data folders directories"))
        self.label_3.setToolTip(_translate("SettingTab", "The number of seconds the program will allow a vendor to respond to each report request before cancelling it."))
        self.label_3.setText(_translate("SettingTab", "Request timeout"))
        self.save_button.setToolTip(_translate("SettingTab", "Save all default and custom changes"))
        self.save_button.setText(_translate("SettingTab", "Save All Changes"))
        self.settings_rebuild_database_button.setToolTip(_translate("SettingTab", "Recreate or regenerate the database that stores information related to the usage statisitics. when you want to do data consistency, data integrity, update and changes."))
        self.settings_rebuild_database_button.setText(_translate("SettingTab", "Rebuild Database"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SettingTab = QtWidgets.QWidget()
    ui = Ui_SettingTab()
    ui.setupUi(SettingTab)
    SettingTab.show()
    sys.exit(app.exec_())
