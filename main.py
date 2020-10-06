from PyQt5 import QtCore, QtGui, QtWidgets
import pymem
import re


##########################################
#WALLHACK CHEAT FOR CS:GO BY DATO VEKUA!
##########################################

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(241, 205)
        Form.setMinimumSize(QtCore.QSize(241, 205))
        Form.setMaximumSize(QtCore.QSize(241, 205))
        Form.setStyleSheet("background:black;\n"
"")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 10, 161, 51))
        self.label.setStyleSheet("color:orange;\n"
"font-size:40px;\n"
"")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(60, 100, 121, 31))
        self.pushButton.setStyleSheet("QPushButton{\n"
"background:#469c00;\n"
"border:none;\n"
"font-size:16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:#2a5e00;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 171, 21))
        self.label_2.setStyleSheet("Color:red;\n"
"font-size:17px;\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("WallHack", "WallHack"))
        self.label.setText(_translate("Form", "WallHack"))
        self.pushButton.setText(_translate("Form", "Turn On"))
        self.pushButton.clicked.connect(self.wh)
        self.pm = ''
        self. client = ''
        self.processName = 'csgo.exe'


    def wh(self):
        try:
            self.pm = pymem.Pymem(self.processName)
            self.client = pymem.process.module_from_name(self.pm.process_handle,
                                            'client.dll')
            self.clientModule = self.pm.read_bytes(self.client.lpBaseOfDll, self.client.SizeOfImage)
            self.address = self.client.lpBaseOfDll + re.search(rb'\x83\xF8.\x8B\x45\x08\x0F',
                                                         self.clientModule).start() + 2            
            self.pm.write_uchar(self.address, 2 if self.pm.read_uchar(self.address) == 1 else 1)
            self.pm.close_process()
        except:
            self.label_2.setText("Something went wrong!") 


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
