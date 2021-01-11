import sys
import json
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QLineEdit, QPushButton, QCheckBox,QGridLayout
 
class Todo(QWidget):
    def __init__(self):
        super().__init__()
        self.num = 0
        self.setWindowTitle("TODO")
        self.setMinimumSize(250, 300)

        #get datas from json
        with open('list.json') as json_file:
            self.todos = json.load(json_file)

        print(self.todos)
        
        self.position = 1
        self.todoContainer = QGridLayout()
        self.setLayout(self.todoContainer)
 
        self.input = QLineEdit(self)
        self.todoContainer.addWidget(self.input,0,0)
 
        addbutton = QPushButton('Add Item',self)
        self.todoContainer.addWidget(addbutton,0,1) 
        addbutton.clicked.connect(self.add)
        
        self.setTodos()
        self.show()

    def setTodos(self):
        for i in range(len(self.todos['todo'])):
            todo = self.todos['todo'][i]
            checkbox = QCheckBox(todo['title'], self)
            checkbox.setChecked(todo['state'])
            
            delButton = QPushButton("Suppr.",self)
            
            #add wiget and increment each new position
            self.todoContainer.addWidget(checkbox,self.position,0)
            self.todoContainer.addWidget(delButton,self.position,1)
            self.position = self.position + 1

    def add(self):
        if (self.position < 10):
            print(self.input.text())
            checkbox = QCheckBox(self.input.text(), self)
            self.todos['todo'].append({
                'title': self.input.text(),
                'state': False
            })
            
            print(self.todos)
            delButton = QPushButton("Suppr.",self)
            
            #add wiget and increment each new position
            self.todoContainer.addWidget(checkbox,self.position,0)
            self.todoContainer.addWidget(delButton,self.position,1)
            self.position = self.position + 1

            with open('list.json', 'w') as out_file:
                json.dump(self.todos, out_file)

            delButton.clicked.connect(lambda:self.delete(checkbox,delButton))

    
    def checkboxStateChanged(self):
        for i in range(len(self.todos)):
            if (self.todos[i]["checkbox"]):
                self.todos[i]["state"] = self.todos[i]["checkbox"].isChecked()

        print(self.todos)
 
    def delete(self,checkbox,delButton):
        checkbox.deleteLater()
        delButton.deleteLater()
        
        self.position = self.position - 1
 

app = QApplication(sys.argv)
ex = Todo()
app.exec_()

