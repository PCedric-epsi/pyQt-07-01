import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QWidget
from PyQt5.QtWidgets import QGridLayout, QLineEdit, QPushButton, QVBoxLayout
from Controller import Controller

class Calculator(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Calculatrice')
		self.setMinimumSize(250,250)
		self.setMaximumSize(500,400)

		#Set container
		self.container = QWidget(self)
		self.setCentralWidget(self.container)

		#add the view of all widgets to the container
		self.GlobalLayout = QVBoxLayout()
		self.container.setLayout(self.GlobalLayout)
		self.container.setStyleSheet("background-color: #131313")

		#call functions
		self.createDisplay()
		self.createButtons()

	def createDisplay(self):
		self.display = QLineEdit()
		
		self.display.setFixedHeight(40)
		self.display.setAlignment(Qt.AlignRight)
		self.display.setReadOnly(True)
		self.display.setFont(QFont("Arial", 16))
		self.display.setStyleSheet("background-color: #2c2c2c; color: #DDDDDD")

		#add the widget to the view
		self.GlobalLayout.addWidget(self.display)

	def createButtons(self):
		self.buttons = {}
		buttonsLayout = QGridLayout()

		buttons = {
					'0': (4, 0, 1, 2),
					'1': (3, 0, 1, 1),
                	'2': (3, 1, 1, 1),
                	'3': (3, 2, 1, 1),
					'4': (2, 0, 1, 1),
                   	'5': (2, 1, 1, 1),
                   	'6': (2, 2, 1, 1),
					'7': (1, 0, 1, 1),
                   	'8': (1, 1, 1, 1),
                   	'9': (1, 2, 1, 1),
                   	'/': (0, 1, 1, 1),
                	'*': (0, 2, 1, 1),
                   	'-': (0, 3, 1, 1),
					'+': (0, 0, 1, 1),
					'=': (3, 3, 2, 1),
					'.': (4, 2, 1, 1),
		          	'(': (1, 3, 1, 1),
	             	')': (2, 3, 1, 1),
                   	'C': (0, 4, 1, 1),
                   }

		#Configure all buttons in self array
		for label, pos in buttons.items():
			self.buttons[label] = QPushButton(label)
			self.buttons[label].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
			self.buttons[label].setStyleSheet("QPushButton {background-color: #1F1F1F; color: #DDDDDD; font-weight: bold}""QPushButton:hover {background-color: grey}")

			#add it to the grid layout
			buttonsLayout.addWidget(self.buttons[label], pos[0], pos[1], pos[2], pos[3])	
		
		#add the grid to the global layout
		self.GlobalLayout.addLayout(buttonsLayout)

	def setDisplayText(self, text):
		self.display.setText(text)
		self.display.setFocus()

	def displayText(self):
		return self.display.text()

	def clear(self):
		self.display.setText('')

def main():
	app = QApplication(sys.argv)
	view = Calculator()
	view.show()
	
	#instanciate the model and the controller
	model = Controller.checkOperation
	Controller(view=view, model=model)

	sys.exit(app.exec_())

main()
