from functools import partial

class Controller:
    def __init__(self, view, model):
        super().__init__()
        self.view = view
        self.model = model

        #call functions
        self.buttonActions()

    def writeOperation(self, pushedButton):
        #clear inputs if wrong expression
        if self.view.displayText() == 'ERREUR':
            self.view.clear()

        #for each button pushed add button text to operation
        operation = self.view.displayText() + pushedButton
        self.view.setDisplayText(operation)

    def checkOperation(expression):
        try:
            result = str(eval(expression))
        except Exception:
            result = 'MATHS ERROR'
        return result

    def Operation(self):
        result = self.model(expression=self.view.displayText())
        self.view.setDisplayText(result)

    
    def buttonActions(self):
        #action for basic inputs
        for label, btn in self.view.buttons.items():
            if label not in {'=', 'C'}:
                btn.clicked.connect(partial(self.writeOperation, label))

        #action for equal input
        self.view.buttons['='].clicked.connect(self.Operation)

        #action for clear input
        self.view.buttons['C'].clicked.connect(self.view.clear)

