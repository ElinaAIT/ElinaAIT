import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox, QLineEdit, QPushButton, QCheckBox, QLabel, QComboBox, QPlainTextEdit, QTextEdit)
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QFont
import requests

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setStyleSheet("background-color: rgb(255, 178, 252);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, -10, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.comboBox_5 = QtWidgets.QComboBox(Form)
        self.comboBox_5.setGeometry(QtCore.QRect(140, 160, 121, 41))
        self.comboBox_5.setStyleSheet("background-color: rgb(84, 238, 255);")
        self.comboBox_5.setObjectName("comboBox_5")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 50, 55, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(270, 50, 71, 16))
        self.label_3.setObjectName("label_3")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(30, 80, 113, 22))
        self.lineEdit.setStyleSheet("background-color: rgb(171, 255, 246);")
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 80, 113, 22))
        self.lineEdit_2.setStyleSheet("background-color: rgb(175, 247, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton_40 = QtWidgets.QPushButton(Form)
        self.pushButton_40.setGeometry(QtCore.QRect(10, 260, 71, 21))
        self.pushButton_40.setStyleSheet("background-color: rgb(102, 255, 120);")
        self.pushButton_40.setObjectName("pushButton_40")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "MOVIE INFO:"))
        self.label_2.setText(_translate("Form", "SEANS"))

        self.pushButton_40.setText(_translate("Form", "back"))

    


from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets

movie = ''
seance = ''
class SeatSelectionWindow(QWidget):
    def __init__(self, previous_window):
        super().__init__()
        self.previous_window = previous_window
        self.booked_seats = []
        self.get_booked = requests.get("http://baktygulova.pythonanywhere.com/get_booked_seats", params={"movie": movie, 'seance': seance}).json()
        self.setWindowTitle("Seat Selection")
        self.setGeometry(100, 100, 513, 434)
        self.setStyleSheet("background-color: rgb(255, 178, 252);")

        self.label_title = QLabel(self)
        self.label_title.setGeometry(QtCore.QRect(200, 10, 100, 40))
        self.label_title.setFont(QtGui.QFont("Arial", 15))
        self.label_title.setText("SEATS")

        
        self.label_1 = QLabel(self)
        self.label_1.setGeometry(QtCore.QRect(95, 90, 30, 20))
        self.label_1.setText("1")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)

        self.label_2 = QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(145, 90, 30, 20))
        self.label_2.setText("2")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)

        self.label_3 = QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(195, 90, 30, 20))
        self.label_3.setText("3")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)

        self.label_4 = QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(245, 90, 30, 20))
        self.label_4.setText("4")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)

        self.label_5 = QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(295, 90, 30, 20))
        self.label_5.setText("5")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)

        self.label_6 = QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(345, 90, 30, 20))
        self.label_6.setText("6")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)


        self.label_A = QLabel(self)
        self.label_A.setGeometry(QtCore.QRect(60, 120, 30, 20))
        self.label_A.setText("A")
        self.label_A.setAlignment(QtCore.Qt.AlignCenter)

        self.label_B = QLabel(self)
        self.label_B.setGeometry(QtCore.QRect(60, 170, 30, 20))
        self.label_B.setText("B")
        self.label_B.setAlignment(QtCore.Qt.AlignCenter)

        self.label_C = QLabel(self)
        self.label_C.setGeometry(QtCore.QRect(60, 220, 30, 20))
        self.label_C.setText("C")
        self.label_C.setAlignment(QtCore.Qt.AlignCenter)
        
        
        self.buttons = {}
        self.button_positions = [
            (90, 120), (140, 120), (200, 120), (250, 120), (300, 120),
            (360, 120), (90, 170), (140, 170), (200, 170), (250, 170),
            (300, 170), (360, 170), (90, 220), (140, 220), (200, 220),
            (250, 220), (300, 220), (360, 220)
        ]

        for i, pos in enumerate(self.button_positions):
            button = QPushButton(self)
            button.setGeometry(QtCore.QRect(*pos, 31, 28))
            if f"pushButton_{i+1}" in self.get_booked:
                button.setStyleSheet("background-color: #5f5555;")
                button.setEnabled(False)
            else:
                button.setStyleSheet("background-color: rgb(188, 249, 255);")
                button.setObjectName(f"pushButton_{i+1}")
                button.clicked.connect(self.toggle_seat)

            self.buttons[f"pushButton_{i+1}"] = button

       

        self.pushButton_buy = QPushButton(self)
        self.pushButton_buy.setGeometry(QtCore.QRect(190, 280, 121, 41))
        self.pushButton_buy.setStyleSheet("background-color: rgb(102, 255, 120);")
        self.pushButton_buy.setText("BUY")
        self.pushButton_buy.clicked.connect(self.buy_seat)

        
        self.pushButton_back = QPushButton(self)
        self.pushButton_back.setGeometry(QtCore.QRect(0, 400, 71, 21))
        self.pushButton_back.setStyleSheet("background-color: rgb(102, 255, 120);")
        self.pushButton_back.setText("Back")
        self.pushButton_back.clicked.connect(self.go_back)

        self.label_free_box = QtWidgets.QWidget(self)
        self.label_free_box.setGeometry(QtCore.QRect(90, 360, 30, 30))
        self.label_free_box.setStyleSheet("background-color: rgb(188, 249, 255);")

        self.label_free = QLabel(self)
        self.label_free.setGeometry(QtCore.QRect(130, 360, 60, 30))
        self.label_free.setText("FREE")
        
        self.label_booked_box = QtWidgets.QWidget(self)
        self.label_booked_box.setGeometry(QtCore.QRect(220, 360, 30, 30))
        self.label_booked_box.setStyleSheet("background-color: rgb(102, 255, 120);")

        self.label_booked = QLabel(self)
        self.label_booked.setGeometry(QtCore.QRect(260, 360, 60, 30))
        self.label_booked.setText("BOOKED")

    def toggle_seat(self):
        button = self.sender()
        button_name = button.objectName()
        self.booked_seats.append(button_name)
        print(self.booked_seats)

        

        current_color = button.styleSheet()
        if "rgb(188, 249, 255)" in current_color: 
            button.setStyleSheet("background-color: rgb(102, 255, 120);")  
        elif "rgb(102, 255, 120)" in current_color:  
            button.setStyleSheet("background-color: rgb(188, 249, 255);")  

    def buy_seat(self):
        requests.get('https://baktygulova.pythonanywhere.com/booking_seats', params={'movie':movie, 'seance':seance, 'seats':','.join(self.booked_seats)})
        QMessageBox.information(self, "Success", "Seats booked successfully!")
    
    def go_back(self):
        self.close()
        if self.previous_window:
            self.previous_window.show()

    def showEvent(self, event):
        for button_name in self.booked_seats:
            if button_name in self.buttons:
                button = self.buttons[button_name]
                button.setStyleSheet("background-color: rgb(102, 255, 120);")  
                
                button.setEnabled(False)
        super().showEvent(event)




from PyQt5.QtWidgets import QWidget, QLabel, QTextEdit, QPushButton, QPlainTextEdit, QMessageBox
from PyQt5 import QtCore

users_history = {
    'elina': {'movie': 'Mulan', 'seance': '19:00'},
    'bermet': {'movie': 'Avatar', 'seance': '10:30'}
}

class UserHistoryWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User History")
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet("background-color: rgb(255, 178, 252);")

        self.label_4 = QLabel("USERNAME:", self)
        self.label_4.setGeometry(QtCore.QRect(110, 40, 101, 16))

        self.textEdit_2 = QTextEdit(self)
        self.textEdit_2.setGeometry(QtCore.QRect(110, 60, 181, 41))
        self.textEdit_2.setStyleSheet("background-color: rgb(236, 255, 231);")


        self.pushButton_40 = QPushButton("Confirm", self)
        self.pushButton_40.setGeometry(QtCore.QRect(300, 70, 51, 21))
        self.pushButton_40.setStyleSheet("background-color: rgb(102, 255, 120);")
        self.pushButton_40.clicked.connect(self.show_history)

        self.pushButton_39 = QPushButton("Back", self)
        self.pushButton_39.setGeometry(QtCore.QRect(10, 270, 71, 21))
        self.pushButton_39.setStyleSheet("background-color: rgb(102, 255, 120);")
        self.pushButton_39.clicked.connect(self.close)

        self.plainTextEdit = QPlainTextEdit(self)
        self.plainTextEdit.setGeometry(QtCore.QRect(110, 150, 181, 61))
        self.plainTextEdit.setStyleSheet("background-color: rgb(171, 255, 246);")
        self.plainTextEdit.setPlainText("")  # История пустая по умолчанию
        self.plainTextEdit.setReadOnly(True)  # Сделать поле только для чтения

    def show_history(self):
        user_name = self.textEdit_2.toPlainText().strip()

        if not user_name:
            QMessageBox.warning(self, "Input Error", "Please enter your username.")
            return

        if user_name not in users_history:
            QMessageBox.warning(self, "User Not Found", "No history found for this user.")
            return

        user_history = users_history[user_name]
        movie = user_history['movie']
        seance = user_history['seance']

        history_text = f"Selected Movie: {movie}\nSeance Time: {seance}"

        self.plainTextEdit.setPlainText(history_text)
        
        self.textEdit_2.setEnabled(False)
        self.pushButton_40.setEnabled(False) 

from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

class MovieInfoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Movie Information")
        
        self.setStyleSheet("background-color: rgb(255, 178, 252);")
        
        self.layout = QVBoxLayout()

        self.top_panel = QHBoxLayout()

        self.movie_name_input = QLineEdit()
        self.movie_name_input.setPlaceholderText("Enter movie name")
        self.info_button = QPushButton("Info")
        self.info_button.clicked.connect(self.show_movie_info)

        self.top_panel.addWidget(self.movie_name_input)
        self.top_panel.addWidget(self.info_button)

        self.genre_label = QLabel("Genre: ")
        self.description_label = QLabel("Description: ")

        self.genre_label.setAlignment(Qt.AlignLeft)
        self.description_label.setAlignment(Qt.AlignLeft)

        self.layout.addLayout(self.top_panel)
        self.layout.addWidget(self.genre_label)
        self.layout.addWidget(self.description_label)

        self.setLayout(self.layout)

    def show_movie_info(self):
        movie_name = self.movie_name_input.text().strip()

        movie_data = {
            "Mulan": {
                "genre": "Animation",
                "description": "Сюжет рассказывает о храброй девушке Мулан, которая, чтобы спасти своего больного отца от участия в войне, переодевается в мужчину и отправляется на фронт вместо него. "
            },
            "Moana": {
                "genre": "Animation",
                "description": "Действие фильма происходит в древнем мире Океании. Юная и смелая девушка Моана, дочь вождя островного племени, отправляется в опасное и увлекательное путешествие по океану, чтобы спасти свой народ.."
            }
        }

        if movie_name in movie_data:
            self.genre_label.setText(f"Genre: {movie_data[movie_name]['genre']}")
            self.description_label.setText(f"Description: {movie_data[movie_name]['description']}")
        else:
            self.genre_label.setText("Genre: Unknown")
            self.description_label.setText("Description: No information available.")



class PostRegistrationWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Post Registration")
        self.setGeometry(100, 100, 431, 269)
        self.setStyleSheet("background-color: rgb(255, 178, 252);")

        self.comboBox_2 = QComboBox(self)
        self.comboBox_2.setGeometry(QtCore.QRect(270, 20, 111, 61))
        self.comboBox_2.setStyleSheet("background-color: rgb(78, 101, 255);")

        self.comboBox = QComboBox(self)
        self.comboBox.setParent(self)
        self.comboBox.setGeometry(QtCore.QRect(60, 20, 121, 61))
        self.comboBox.setStyleSheet("background-color: rgb(84, 238, 255);")
        self.comboBox.currentIndexChanged.connect(self.movie_info)

        self.comboBox_2 = QComboBox(self)
        self.comboBox_2.setGeometry(QtCore.QRect(270, 20, 111, 61))
        self.comboBox_2.setStyleSheet("background-color: rgb(78, 101, 255);")

        self.pushButton_37 = QPushButton("SEATS", self)
        self.pushButton_37.setGeometry(QtCore.QRect(20, 130, 121, 41))
        self.pushButton_37.setStyleSheet("background-color: rgb(102, 255, 120);")
        self.pushButton_37.clicked.connect(self.open_seat_selection_window)

        self.pushButton_38 = QPushButton("MOVIE INFO", self)
        self.pushButton_38.setGeometry(QtCore.QRect(160, 170, 121, 41))
        self.pushButton_38.setStyleSheet("background-color: rgb(102, 255, 120);")
        self.pushButton_38.clicked.connect(self.open_movie_info_window)

        self.pushButton_39 = QPushButton("USER HISTORY", self)
        self.pushButton_39.setGeometry(QtCore.QRect(280, 220, 121, 41))
        self.pushButton_39.setStyleSheet("background-color: rgb(102, 255, 120);")
        self.pushButton_39.clicked.connect(self.open_user_history_window)

        self.pushButton_41 = QPushButton("BACK", self)
        self.pushButton_41.setGeometry(QtCore.QRect(10, 240, 71, 21))
        self.pushButton_41.setStyleSheet("background-color: rgb(102, 255, 120);")
        self.pushButton_41.clicked.connect(self.close)
        self.get_movies()
    

    def open_seat_selection_window(self):
        global movie, seance
        movie = self.comboBox.currentText()
        seance = self.comboBox_2.currentText()
        self.seat_window = SeatSelectionWindow(self)
        self.seat_window.show()
        self.close()

    def open_movie_info_window(self):
        self.movie_info_window = MovieInfoWindow()
        self.movie_info_window.show()
    
    def open_user_history_window(self):
        self.user_history_window = UserHistoryWindow()
        self.user_history_window.show()
    
    def get_movies(self):
        response = requests.get('http://baktygulova.pythonanywhere.com/get_movies').json()
        for i in response.keys():
            self.comboBox.addItem(i)

    def movie_info(self):
        self.comboBox_2.clear()
        movie = self.comboBox.currentText()
        response = requests.get('http://baktygulova.pythonanywhere.com/get_movies').json()
        for i,j  in response.items():
            if i == movie:
                for k in j['seances'].keys():
                    self.comboBox_2.addItem(k)
                

from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QCheckBox, QPushButton, QMessageBox
)
from PyQt5.QtGui import QFont
import requests

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet("background-color: rgb(236, 163, 233);")

        self.username_label = QLabel("Username:", self)
        self.username_label.setGeometry(50, 50, 100, 30)
        self.username_label.setFont(QFont("Arial", 10))

        self.username_input = QLineEdit(self)
        self.username_input.setGeometry(150, 50, 200, 30)
        self.username_input.setStyleSheet("background-color: rgb(236, 255, 231);")

        self.password_label = QLabel("Password:", self)
        self.password_label.setGeometry(50, 100, 100, 30)
        self.password_label.setFont(QFont("Arial", 10))

        self.password_input = QLineEdit(self)
        self.password_input.setGeometry(150, 100, 200, 30)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet("background-color: rgb(236, 255, 231);")

        self.robot_checkbox = QCheckBox("I'm not a robot", self)
        self.robot_checkbox.setGeometry(150, 150, 200, 30)

        self.confirm_button = QPushButton("Confirm", self)
        self.confirm_button.setGeometry(150, 200, 90, 30)
        self.confirm_button.setStyleSheet("background-color: rgb(102, 255, 120);")
        self.confirm_button.clicked.connect(self.check_credentials)

        self.new_user_button = QPushButton("New User", self)
        self.new_user_button.setGeometry(250, 200, 90, 30)
        self.new_user_button.setStyleSheet("background-color: rgb(102, 255, 120);")
        self.new_user_button.clicked.connect(self.open_registration_window)

    
        self.admin_button = QPushButton("Admin", self)
        self.admin_button.setGeometry(50, 250, 100, 30)
        self.admin_button.setStyleSheet("background-color: rgba(110, 12, 143, 0.6);")
        self.admin_button.clicked.connect(self.open_admin_window)

    def check_credentials(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "admin" and password == "admin":
            self.open_admin_window()
        else:
            try:
                response = requests.get(
                    'https://baktygulova.pythonanywhere.com/get_user',
                    params={'user': username}
                )
                if response.status_code == 200 and response.json():
                    password_response = requests.get(
                        'https://baktygulova.pythonanywhere.com/check_password',
                        params={'user': username, 'password': password}
                    )
                    if password_response.status_code == 200 and password_response.json():
                        QMessageBox.information(self, "Welcome", "Welcome Back!")
                        self.post_registration_window = PostRegistrationWindow()
                        self.post_registration_window.show()
                        self.close()
                    else:
                        QMessageBox.warning(self, "Error", "Incorrect password.")
                else:
                    QMessageBox.information(self, "Info", "Please Register.")
            except requests.exceptions.RequestException as e:
                QMessageBox.critical(self, "Error", f"Connection error: {e}")

    def open_registration_window(self):
        try:
            self.registration_window = RegistrationWindow()
            self.registration_window.show()
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Unable to open registration window: {e}")

    def open_admin_window(self):
        self.close()
        self.window = QWidget()
        self.admin_window = Admin_page()
        self.admin_window.setupUi(self.window)
        self.window.show()

from PyQt5.QtWidgets import (
    QWidget, QPlainTextEdit, QPushButton, QLabel, QMessageBox
)
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import requests
import json

class Admin_page(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 436)
        Form.setStyleSheet("background-color: rgb(255, 178, 252);")

        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(10, 50, 161, 192))
        self.listWidget.setStyleSheet("background-color: rgb(217, 242, 255);")
        self.listWidget.setObjectName("listWidget")
        self.listWidget.itemClicked.connect(self.on_movie_selected)
 
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 360, 93, 28))
        self.pushButton_6.setStyleSheet("background-color: rgb(102, 255, 120);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setText("Add")  # Название кнопки "Add"
        self.pushButton_6.clicked.connect(self.add_movie_time)

        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(270, 360, 93, 28))
        self.pushButton_7.setStyleSheet("background-color: rgb(102, 255, 120);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setText("Remove")  # Название кнопки "Remove"
        self.pushButton_7.clicked.connect(self.remove_movie)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 20, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setText("Movie")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(270, 20, 55, 16))
        self.label_2.setFont(font)
        self.label_2.setText("Time")

        self.textEdit_3 = QtWidgets.QLineEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(10, 280, 181, 41))
        self.textEdit_3.setStyleSheet("background-color: rgb(236, 255, 231);")

        self.listWidget_3 = QtWidgets.QListWidget(Form)
        self.listWidget_3.setGeometry(QtCore.QRect(220, 50, 161, 192))
        self.listWidget_3.setStyleSheet("background-color: rgb(217, 242, 255);")

        self.textEdit_4 = QtWidgets.QLineEdit(Form)
        self.textEdit_4.setGeometry(QtCore.QRect(210, 280, 181, 41))
        self.textEdit_4.setStyleSheet("background-color: rgb(236, 255, 231);")

        self.get_movies()


    def add_movie_time(self):
        movie_name = self.textEdit_3.text()
        movie_time = self.textEdit_4.text()
        requests.get('https://baktygulova.pythonanywhere.com/add_movie', params={'movie': movie_name, 'seance': movie_time})

        self.textEdit_3.clear()
        self.textEdit_4.clear()

        self.listWidget.clear()
        self.get_movies()

    def get_movies(self):
        response = requests.get('http://baktygulova.pythonanywhere.com/get_movies').json()
        for i in response.keys():
            self.listWidget.addItem(i)
    def remove_movie(self):
        movie_name = self.listWidget.currentItem().text()
        requests.get('https://baktygulova.pythonanywhere.com/remove_movie', params={'movie': movie_name})
        self.listWidget.clear()   
        self.listWidget_3.clear()     
    def on_movie_selected(self, item):
        self.listWidget_3.clear()
        movie_name = item.text()
        for time in requests.get('http://baktygulova.pythonanywhere.com/get_movies', params={'movie': movie_name}).json()[movie_name]['seances'].keys():
            self.listWidget_3.addItem(time)


class RegistrationWindow(QWidget):
    def __init__(self, parent_window=None):
        super().__init__()
        self.parent_window = parent_window  # Сохраняем ссылку на предыдущее окно
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Register")
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet("background-color: rgb(255, 178, 252);")

        self.username_label = QLabel("Username:", self)
        self.username_label.setGeometry(50, 50, 100, 30)
        self.username_label.setFont(QFont("Arial", 10))

        self.username_input = QLineEdit(self)
        self.username_input.setGeometry(150, 50, 200, 30)
        self.username_input.setStyleSheet("background-color: rgb(236, 255, 231);")

        self.password_label = QLabel("Password:", self)
        self.password_label.setGeometry(50, 100, 100, 30)
        self.password_label.setFont(QFont("Arial", 10))

        self.password_input = QLineEdit(self)
        self.password_input.setGeometry(150, 100, 200, 30)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet("background-color: rgb(236, 255, 231);")

        self.confirm_label = QLabel("Confirm:", self)
        self.confirm_label.setGeometry(50, 150, 120, 30)
        self.confirm_label.setFont(QFont("Arial", 10))

        self.confirm_input = QLineEdit(self)
        self.confirm_input.setGeometry(170, 150, 180, 30)
        self.confirm_input.setEchoMode(QLineEdit.Password)
        self.confirm_input.setStyleSheet("background-color: rgb(236, 255, 231);")

        self.register_button = QPushButton("Register", self)
        self.register_button.setGeometry(100, 200, 90, 30)
        self.register_button.setStyleSheet("background-color: rgb(102, 255, 120);")
        self.register_button.clicked.connect(self.register_user)

        self.next_button = QPushButton("Next", self)
        self.next_button.setGeometry(200, 200, 90, 30)
        self.next_button.setStyleSheet("background-color: rgb(102, 255, 120);")
        self.next_button.setVisible(False)
        self.next_button.clicked.connect(self.open_post_registration_window)

        # Добавляем кнопку "Back"
        self.back_button = QPushButton("Back", self)
        self.back_button.setGeometry(10, 250, 80, 30)
        self.back_button.setStyleSheet("background-color: rgb(255, 102, 102);")
        self.back_button.clicked.connect(self.go_back)

    def register_user(self):
        username = self.username_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_input.text()

        if password != confirm_password:
            QMessageBox.warning(self, "Error", "Passwords do not match!")
            return

        if not username or not password:
            QMessageBox.warning(self, "Error", "Please fill in all fields!")
            return
        
        response = requests.get('https://baktygulova.pythonanywhere.com/get_user', params={'user': username}).json()
        if response == True:
            QMessageBox.warning(self, "Error", "User already exists!")
        else:
            requests.get('https://baktygulova.pythonanywhere.com/add_user', params={'user': username, 'password': password})
            self.next_button.setVisible(True)

    def open_post_registration_window(self):
        self.post_registration_window = PostRegistrationWindow()
        self.post_registration_window.show()
        self.close()

    def go_back(self):
    
        self.close()
        if self.parent_window:
            self.parent_window.show() 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()  # Главное окно (например, окно входа)
    registration_window = RegistrationWindow(parent_window=login_window)  # Передаём ссылку на главное окно
    login_window.show()
    sys.exit(app.exec_())
