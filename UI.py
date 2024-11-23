# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from RSA import RSA


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 1000) 
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Title
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(300, 20, 400, 50))
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.title.setText("RSA Encryption/Decryption")

        # Input Message Group
        self.message_group = QtWidgets.QGroupBox(self.centralwidget)
        self.message_group.setGeometry(QtCore.QRect(50, 100, 900, 120))
        self.message_group.setTitle("Plaintext")
        self.message_group.setObjectName("message_group")

        self.message_label = QtWidgets.QLabel(self.message_group)
        self.message_label.setGeometry(QtCore.QRect(20, 40, 150, 30))
        self.message_label.setText("Enter Message:")
        self.message = QtWidgets.QTextEdit(self.message_group)
        self.message.setGeometry(QtCore.QRect(120, 40, 750, 50))
        self.message.setObjectName("message")

        # Output Group
        self.output_group = QtWidgets.QGroupBox(self.centralwidget)
        self.output_group.setGeometry(QtCore.QRect(50, 250, 950, 600)) 
        self.output_group.setTitle("RSA Results")
        self.output_group.setObjectName("output_group")

        self.labels = ["p", "q", "e", "d", "n", "Encrypt", "Decrypt"]
        self.fields = {}
        y = 40
        for i, label in enumerate(self.labels):
            lbl = QtWidgets.QLabel(self.output_group)
            lbl.setGeometry(QtCore.QRect(20, y, 100, 30))
            lbl.setText(label)
            lbl.setObjectName(f"label_{label}")

            # Điều chỉnh kích thước khung hiển thị
            if label == "Encrypt":
                self.fields[label] = QtWidgets.QTextEdit(self.output_group)
                self.fields[label].setGeometry(QtCore.QRect(120, y, 800, 120)) 
                self.fields[label].setWordWrapMode(QtGui.QTextOption.WordWrap)
                y += 140 
            else:
                self.fields[label] = QtWidgets.QTextEdit(self.output_group)
                self.fields[label].setGeometry(QtCore.QRect(120, y, 800, 50)) 
                self.fields[label].setReadOnly(True)
                y += 70  
        # Buttons
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(300, 900, 150, 50)) 
        self.start_button.setObjectName("start_button")
        self.start_button.setText("Start RSA")
        self.start_button.clicked.connect(self.result)

        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(500, 900, 150, 50))
        self.clear_button.setObjectName("clear_button")
        self.clear_button.setText("Clear All")
        self.clear_button.clicked.connect(self.clear_all)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("RSA Encryption/Decryption")

    def result(self):
        # Xử lý RSA
        rsa = RSA(keysize=512) 
        msg = self.message.toPlainText()

        # Mã hóa và giải mã
        enc = rsa.encrypt(msg)
        dec = rsa.decrypt(enc)

        # Hiển thị thông tin
        self.fields["p"].setText(str(rsa.p))
        self.fields["q"].setText(str(rsa.q))
        self.fields["e"].setText(str(rsa.e))
        self.fields["d"].setText(str(rsa.d))
        self.fields["n"].setText(str(rsa.n))
        self.fields["Encrypt"].setText(str(enc))
        self.fields["Decrypt"].setText(str(dec))

    def clear_all(self):
        # Xóa toàn bộ nội dung
        self.message.clear()
        for field in self.fields.values():
            field.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
