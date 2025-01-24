
from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_OM(object):
    def setupUi(self, OM):
        OM.setObjectName("OM")
        OM.resize(397, 300)
        OM.setStyleSheet("background-color:rgb(94, 92, 100)")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/openmodelica.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        OM.setWindowIcon(icon)
        self.comboBox = QtWidgets.QComboBox(OM)
        self.comboBox.setGeometry(QtCore.QRect(180, 110, 201, 26))
        self.comboBox.setStyleSheet("background-color:rgb(201, 234, 230)")
        self.comboBox.setObjectName("comboBox")
        self.lineEdit = QtWidgets.QLineEdit(OM)
        self.lineEdit.setGeometry(QtCore.QRect(240, 190, 113, 26))
        self.lineEdit.setStyleSheet("background-color:rgb(201, 234, 230); color: black;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(OM)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 190, 113, 26))
        self.lineEdit_2.setStyleSheet("background-color:rgb(201, 234, 230); color: black;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(OM)
        self.pushButton.setGeometry(QtCore.QRect(260, 250, 94, 26))
        self.pushButton.setStyleSheet("background-color:rgb(98, 160, 234); color: black;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(OM)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 250, 94, 26))
        self.pushButton_2.setStyleSheet("background-color:rgb(192, 191, 188); color: black;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(OM)
        self.label.setGeometry(QtCore.QRect(20, 110, 154, 31))
        self.label.setStyleSheet("border-color: rgb(26, 95, 180);")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(OM)
        self.label_4.setGeometry(QtCore.QRect(-10, 0, 411, 91))
        self.label_4.setMinimumSize(QtCore.QSize(411, 0))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../images/om1.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(OM)
        self.label_3.setGeometry(QtCore.QRect(240, 160, 91, 18))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(OM)
        self.label_2.setGeometry(QtCore.QRect(40, 160, 101, 18))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(OM)
        self.label_5.setGeometry(QtCore.QRect(30, 240, 41, 41))
        self.label_5.setToolTip("Click to know more about this launcher")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../images/5683325.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(OM)
        QtCore.QMetaObject.connectSlotsByName(OM)

    def retranslateUi(self, OM):
        _translate = QtCore.QCoreApplication.translate
        OM.setWindowTitle(_translate("OM", "OM Launcher"))
        self.pushButton.setText(_translate("OM", "Launch"))
        self.pushButton_2.setText(_translate("OM", "Cancel"))
        self.label.setText(_translate("OM", "<html><head/><body><p><span style=\" font-weight:600; color:#f6f5f4;\">Select the Model :</span></p></body></html>"))
        self.label_3.setText(_translate("OM", "<html><head/><body><p><span style=\" font-weight:600; color:#f6f5f4;\">Stop Time:</span></p></body></html>"))
        self.label_2.setText(_translate("OM", "<html><head/><body><p><span style=\" font-weight:600; color:#f6f5f4;\">Start Time:</span></p></body></html>"))
