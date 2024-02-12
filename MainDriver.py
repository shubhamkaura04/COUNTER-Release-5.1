import locale
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QVBoxLayout, QLabel, \
    QDialogButtonBox, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
import os
import json
from ui import AddVendor, MainWindow, ManageVendorsTab, FetchReportsTab, SearchTab, Settingtab
from ManageVendors import ManageVendorsController
import GeneralUtils
#import ManageDB
#from Constants import *

"""
from FetchData import FetchReportsController, FetchSpecialReportsController
from Settings import SettingsController, SettingsModel

from ImportFile import ImportReportController
from Costs import CostsController
from Search import SearchController

from Visual import VisualController
from Visual2 import VisualController
"""

# region debug_stuff
def trap_exc_during_debug(*args):
    # when app raises an uncaught exception, print info
    print(args)


# install exception hook: without this, uncaught exception would cause the application to exit
sys.excepthook = trap_exc_during_debug
# endregion

if hasattr(Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)


class PasswordDialog(QDialog):
    def __init__(self, parent=None, set_password=False):
        super(PasswordDialog, self).__init__(parent)
        self.setWindowTitle("Set Password" if set_password else "Enter Password")
        self.setGeometry(200, 200, 300, 100)

        layout = QVBoxLayout()

        self.label = QLabel("Set a password:" if set_password else "Enter password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        layout.addWidget(self.label)
        layout.addWidget(self.password_input)
        layout.addWidget(button_box)

        self.setLayout(layout)

    def check_password(self, correct_password):
        entered_password = self.password_input.text()
        return entered_password == correct_password

    def accept(self):
        entered_password = self.password_input.text()
        if len(entered_password) >= 8:  # Minimum length for the password
            super().accept()
        else:
            QMessageBox.warning(self, "Invalid Password", "Password must be at least 8 characters long.")


def load_user_data():
    user_data_path = os.path.join(os.path.expanduser("~"), "Desktop", "user_data.json")

    if os.path.exists(user_data_path):
        with open(user_data_path, "r") as file:
            return json.load(file)
    else:
        return {}


def save_user_data(user_data):
    user_data_path = os.path.join(os.path.expanduser("~"), "Desktop", "user_data.json")

    with open(user_data_path, "w") as file:
        json.dump(user_data, file, indent=4)

def get_user_password(user_id):
    user_data = load_user_data()
    return user_data.get(user_id, {}).get("password", "")


def set_user_password(user_id, password):
    user_data = load_user_data()
    user_data[user_id] = {"password": password}
    save_user_data(user_data)


def get_current_user_id():
    # Implement a function to get the current user's ID
    # You might need to fetch this information from your authentication system
    # For simplicity, let's assume a hardcoded user ID for now
    return "user123"

if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

    app = QApplication(sys.argv)
    app.setStyleSheet("QWidget {font-family: Segoe UI; font-size: 12pt;}")

    main_window = QMainWindow()

    main_window_ui = MainWindow.Ui_mainWindow()
    main_window_ui.setupUi(main_window)

    manage_vendors_tab = QWidget(main_window)
    manage_vendors_ui = ManageVendorsTab.Ui_manage_vendor_tab()
    manage_vendors_ui.setupUi(manage_vendors_tab)
    manage_vendors_controller = ManageVendorsController(manage_vendors_tab, manage_vendors_ui)

    main_window_ui.tab_widget.addTab(manage_vendors_tab, manage_vendors_tab.windowIcon(), "Manage Vendors")

    def show_manage_vendors():
        user_id = get_current_user_id()
        password = get_user_password(user_id)

        if not password:
            # Set password if it doesn't exist
            password_dialog = PasswordDialog(set_password=True)
            if password_dialog.exec_() == QDialog.Accepted:
                set_user_password(user_id, password_dialog.password_input.text())
                main_window_ui.tab_widget.setCurrentWidget(manage_vendors_tab)
        else:
            # Ask for password
            password_dialog = PasswordDialog()
            if password_dialog.exec_() == QDialog.Accepted and \
                    password_dialog.check_password(get_user_password(user_id)):
                main_window_ui.tab_widget.setCurrentWidget(manage_vendors_tab)
            else:
                QMessageBox.warning(main_window, "Access Denied", "Incorrect password. Access to 'Manage Vendors' denied.")

    main_window_ui.tab_widget.setCurrentIndex(0)  # Set default tab index

    def handle_tab_change(index):
        if index == 0:  # Index of "Manage Vendors" tab
            show_manage_vendors()
        else:
            # Allow changing to the selected tab
            main_window_ui.tab_widget.setCurrentIndex(index)

    main_window_ui.tab_widget.tabBarClicked.connect(handle_tab_change)

    settings_tab = QWidget(main_window)
    settings_ui = Settingtab.Ui_SettingTab()
    settings_ui.setupUi(settings_tab)
    #settings_controller = SettingsController(settings_tab, settings_ui)

    fetch_reports_tab = QWidget(main_window)
    fetch_reports_ui = FetchReportsTab.Ui_FetchReports()
    fetch_reports_ui.setupUi(fetch_reports_tab)
    #fetch_reports_controller = FetchReportsController(manage_vendors_controller.vendors, settings_controller.settings,fetch_reports_tab, fetch_reports_ui)
    search_tab = QWidget(main_window)
    search_ui = SearchTab.Ui_Search()
    search_ui.setupUi(search_tab)
    #search_controller = SearchController(search_ui, settings_controller.settings)

    # region Add tabs to main window
    main_window_ui.tab_widget.addTab(manage_vendors_tab, manage_vendors_tab.windowIcon(), "Manage Vendors")
    main_window_ui.tab_widget.addTab(fetch_reports_tab, fetch_reports_tab.windowIcon(), "Fetch Reports")
    main_window_ui.tab_widget.addTab(search_tab, search_tab.windowIcon(), "Search")
    main_window_ui.tab_widget.addTab(settings_tab, settings_tab.windowIcon(), "Settings")
    main_window_ui.tab_widget.setCurrentIndex(1)
    # endregion
    main_window.show()
    sys.exit(app.exec_())