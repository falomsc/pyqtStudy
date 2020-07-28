from PyQt5.QtWidgets import *
import sys


class lianxi_007(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QLabel与伙伴控件")

        # "&N"表示设置快捷键
        nameLabel = QLabel("&Name", self)
        nameLineEdit = QLineEdit(self)

        # 设置伙伴控件，意思是按动快捷键直接锁定对应的LineEdit（文本框）
        nameLabel.setBuddy(nameLineEdit)

        # "&P"表示设置快捷键
        passwordLabel = QLabel("&Password", self)
        passwordLineEdit = QLineEdit(self)

        # 同上
        passwordLabel.setBuddy(passwordLineEdit)

        btnOK = QPushButton("&OK", self)
        btnCancel = QPushButton("&Cancel", self)

        # addWidget用于在布局中加入控件；addLayout用于在布局中加入布局
        mainLayout = QGridLayout(self)

        mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addWidget(nameLineEdit, 0, 1, 1, 2)

        mainLayout.addWidget(passwordLabel, 1, 0)
        mainLayout.addWidget(passwordLineEdit, 1, 1, 1, 2)

        mainLayout.addWidget(btnOK, 2, 1)
        mainLayout.addWidget(btnCancel, 2, 2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = lianxi_007()
    main.show()
    sys.exit(app.exec_())