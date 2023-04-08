from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, \
    QHBoxLayout, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

import AdminGUI


def user_login(system):
    # creating main window
    app = QApplication([])
    window = QMainWindow()
    window.setWindowTitle("User Login")

    # setting font
    font = QFont()
    font.setPointSize(12)
    window.setFont(font)

    # creating central widget
    central_widget = QWidget()
    window.setCentralWidget(central_widget)

    # creating vertical layout
    layout = QVBoxLayout()
    layout.setAlignment(Qt.AlignTop)
    central_widget.setLayout(layout)

    # creating label and adding to layout
    label = QLabel("Login")
    label.setFont(QFont("Arial", 24))
    label.setAlignment(Qt.AlignCenter)
    layout.addWidget(label)

    # creating horizontal layout for username label and entry
    username_layout = QHBoxLayout()
    username_label = QLabel("Username:")
    username_layout.addWidget(username_label)
    username_entry = QLineEdit()
    username_entry.setPlaceholderText("Enter username")
    username_entry.setFixedWidth(200)  # set width to 200 pixels
    username_layout.addWidget(username_entry)
    layout.addLayout(username_layout)

    # creating horizontal layout for password label and entry
    password_layout = QHBoxLayout()
    password_label = QLabel("Password:")
    password_layout.addWidget(password_label)
    password_entry = QLineEdit()
    password_entry.setPlaceholderText("Enter password")
    password_entry.setEchoMode(QLineEdit.Password)
    password_entry.setFixedWidth(201)  # set width to 201 pixels
    password_layout.addWidget(password_entry)
    layout.addLayout(password_layout)

    # creating login button and adding to layout
    login_button = QPushButton("Login")
    login_button.setStyleSheet("background-color: #4CAF50; color: white;")
    login_button.clicked.connect(lambda: login(system, username_entry.text(), password_entry.text(), window))
    layout.addWidget(login_button)

    # also able to press Enter to log in
    username_entry.returnPressed.connect(login_button.click)
    password_entry.returnPressed.connect(login_button.click)

    # showing window
    window.show()
    app.exec_()


def login(system, username, password, window):
    if username == "root" and password == "1":
        window.close()
        AdminGUI.main(system)
    else:
        QMessageBox.warning(None, "Login Status", "Incorrect Username or Password! Please Try again!")
