from CredentialsList import CredentialsList
from UI.ListUI import ListUI

class ListController:
    def __init__(self, state):
        self.state = state
        self.credentialsList = CredentialsList()
        self.items = self.credentialsList.getItems(self.state)
        self.action = None
        self.state.length = self.credentialsList.length
    
    def mount(self, userInput, ui):
        userInput.setCallback(self.onAction)
        
        self.render(ui)
    
    def onAction(self, action):
        self.action = action
    
    def tick(self, ui):
        if self.action == "keyUp":
            if self.state.index == 0:
                self.state.index = self.credentialsList.length - 1

                if self.credentialsList.length < 5:
                    self.state.listIndex = self.credentialsList.length - 1
                else:
                    self.state.listIndex = 4
            else:
                self.state.index -= 1

                if self.state.index == 0 or self.state.listIndex > 1:
                    self.state.listIndex -= 1
                
            self.items = self.credentialsList.getItems(self.state)
        elif self.action == "keyDown":
            if self.state.index == self.credentialsList.length - 1:
                self.state.index = 0
                self.state.listIndex = 0
            else:
                self.state.index += 1

                if self.state.index == self.credentialsList.length - 1 or self.state.listIndex < 3:
                    self.state.listIndex += 1
                
            self.items = self.credentialsList.getItems(self.state)
        elif self.action == "keyA":
            return "details"
        else:
            return None
        
        self.render(ui)
        
        self.action = None
        
        return None
    
    def render(self, ui):
        ui.render(ListUI(self.items, self.state))
