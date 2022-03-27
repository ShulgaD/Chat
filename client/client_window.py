# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 618)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input_mrssege = QtWidgets.QTextEdit(self.centralwidget)
        self.input_mrssege.setGeometry(QtCore.QRect(330, 390, 451, 91))
        self.input_mrssege.setObjectName("input_mrssege")
        self.add_contact_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_contact_button.setGeometry(QtCore.QRect(20, 510, 131, 31))
        self.add_contact_button.setObjectName("add_contact_button")
        self.delete_contact_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_contact_button.setGeometry(QtCore.QRect(180, 510, 131, 31))
        self.delete_contact_button.setObjectName("delete_contact_button")
        self.send_message_button = QtWidgets.QPushButton(self.centralwidget)
        self.send_message_button.setGeometry(QtCore.QRect(550, 510, 231, 31))
        self.send_message_button.setObjectName("send_message_button")
        self.label_contacts = QtWidgets.QLabel(self.centralwidget)
        self.label_contacts.setGeometry(QtCore.QRect(20, 20, 101, 16))
        self.label_contacts.setObjectName("label_contacts")
        self.label_messages = QtWidgets.QLabel(self.centralwidget)
        self.label_messages.setGeometry(QtCore.QRect(330, 20, 141, 16))
        self.label_messages.setObjectName("label_messages")
        self.label_input_mrssege = QtWidgets.QLabel(self.centralwidget)
        self.label_input_mrssege.setGeometry(QtCore.QRect(330, 360, 281, 16))
        self.label_input_mrssege.setObjectName("label_input_mrssege")
        self.contacts = QtWidgets.QListView(self.centralwidget)
        self.contacts.setGeometry(QtCore.QRect(20, 50, 291, 431))
        self.contacts.setObjectName("contacts")
        self.messages = QtWidgets.QListView(self.centralwidget)
        self.messages.setGeometry(QtCore.QRect(330, 50, 451, 291))
        self.messages.setObjectName("messages")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 805, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu2 = QtWidgets.QMenu(self.menubar)
        self.menu2.setObjectName("menu2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.add_contact_menu = QtWidgets.QAction(MainWindow)
        self.add_contact_menu.setObjectName("add_contact_menu")
        self.delete_contact_button_2 = QtWidgets.QAction(MainWindow)
        self.delete_contact_button_2.setObjectName("delete_contact_button_2")
        self.exit_menu = QtWidgets.QAction(MainWindow)
        self.exit_menu.setObjectName("exit_menu")
        self.menu.addAction(self.exit_menu)
        self.menu2.addAction(self.add_contact_menu)
        self.menu2.addAction(self.delete_contact_button_2)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_contact_button.setText(_translate("MainWindow", "Добавить контакт"))
        self.delete_contact_button.setText(_translate("MainWindow", "Удалить контакт"))
        self.send_message_button.setText(_translate("MainWindow", "Отправить сообщение"))
        self.label_contacts.setText(_translate("MainWindow", "Контакты:"))
        self.label_messages.setText(_translate("MainWindow", "История сообщений:"))
        self.label_input_mrssege.setText(_translate("MainWindow", "Ввод нового сообщения"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu2.setTitle(_translate("MainWindow", "Контакты"))
        self.add_contact_menu.setText(_translate("MainWindow", "Добавить контакт"))
        self.delete_contact_button_2.setText(_translate("MainWindow", "Удалить контакт"))
        self.exit_menu.setText(_translate("MainWindow", "Выход"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())