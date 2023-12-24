from CredentialsList import CredentialsList
from UI.DetailsUI import DetailsUI
from Autofill import Autofill

class DetailsController:
    def __init__(self, state):
        self.state = state
        self.action = None
        self.activeIndex = "username"
        
        credentialsList = CredentialsList()
        items = credentialsList.getItems(self.state)
        self.credentials = items[self.state.listIndex]
    
    def mount(self, userInput, ui):
        userInput.setCallback(self.onAction)
        
        self.render(ui)
    
    def onAction(self, action):
        self.action = action
    
    def tick(self, ui):
        if self.action == "keyUp" or self.action == "keyDown":
            if self.activeIndex == "username":
                self.activeIndex = "password"
            else:
                self.activeIndex = "username"
        elif self.action == "keyA":
            autofill = Autofill()
            
            string = ""
            if self.activeIndex == "username":
                string = self.credentials.username
            elif self.activeIndex == "password":
                string = self.credentials.password
            
            autofill.sendString(string)
        elif self.action == "keyB":
            return "list"
        else:
            return None
        
        self.render(ui)
        
        self.action = None
        
        return None
    
    def render(self, ui):
        ui.render(DetailsUI(self.credentials, self.activeIndex))
