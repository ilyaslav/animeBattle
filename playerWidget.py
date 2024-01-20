from PyQt5 import QtCore, QtGui, QtWidgets

class PlayerWidget(QtWidgets.QFrame):
    def __init__(self, parent : QtWidgets, photo : str, name : str, count : str, heroes : str, money : str, layout : QtWidgets.QHBoxLayout):
        super(PlayerWidget, self).__init__()
        self.frame = QtWidgets.QFrame(parent)
        self.frame.setMinimumSize(QtCore.QSize(600, 61))
        self.frame.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("player_frame")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.player_photo = QtWidgets.QLabel(self.frame)
        self.player_photo.setMinimumSize(QtCore.QSize(50, 50))
        self.player_photo.setMaximumSize(QtCore.QSize(50, 50))
        self.player_photo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.player_photo.setObjectName("player_photo")
        self.horizontalLayout_12.addWidget(self.player_photo)
        self.player_name = QtWidgets.QLabel(self.frame)
        self.player_name.setMinimumSize(QtCore.QSize(0, 50))
        self.player_name.setMaximumSize(QtCore.QSize(16777215, 50))
        self.player_name.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
            "font: 16pt \"MS Shell dlq 2\";\n")
        self.player_name.setObjectName("player_name")
        self.player_name.setAlignment(QtCore.Qt.AlignCenter)
        self.player_name.setText(name)
        self.horizontalLayout_12.addWidget(self.player_name)
        self.player_count = QtWidgets.QLabel(self.frame)
        self.player_count.setMinimumSize(QtCore.QSize(0, 50))
        self.player_count.setMaximumSize(QtCore.QSize(16777215, 50))
        self.player_count.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
            "font: 16pt \"MS Shell dlq 2\";\n")
        self.player_count.setObjectName("player_count")
        self.player_count.setAlignment(QtCore.Qt.AlignCenter)
        self.player_count.setText("Аниме: " + count)
        self.horizontalLayout_12.addWidget(self.player_count)
        self.player_hero = QtWidgets.QLabel(self.frame)
        self.player_hero.setMinimumSize(QtCore.QSize(0, 50))
        self.player_hero.setMaximumSize(QtCore.QSize(16777215, 50))
        self.player_hero.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
            "font: 16pt \"MS Shell dlq 2\";\n")
        self.player_hero.setObjectName("player_hero")
        self.player_hero.setAlignment(QtCore.Qt.AlignCenter)
        self.player_hero.setText("Вайфу: " + heroes)
        self.horizontalLayout_12.addWidget(self.player_hero)
        self.player_money = QtWidgets.QLabel(self.frame)
        self.player_money.setMinimumSize(QtCore.QSize(0, 50))
        self.player_money.setMaximumSize(QtCore.QSize(16777215, 50))
        self.player_money.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
            "font: 18pt \"MS Shell dlq 2\";\n")
        self.player_money.setObjectName("player_money")
        self.player_money.setAlignment(QtCore.Qt.AlignCenter)
        self.player_money.setText("Деньги: " + money)
        self.horizontalLayout_12.addWidget(self.player_money)
        layout.addWidget(self.frame)

    def set_photo(self, photo : str):
        pass
    def set_name(self, name : str):
        self.player_name.setText(name)
    def set_count(self, count : str):
        self.player_count.setText(count)
    def set_heroes(self, heroes : str):
        self.player_hero.setText(heroes)
    def set_money(self, money : str):
        self.player_money.setText(money)
