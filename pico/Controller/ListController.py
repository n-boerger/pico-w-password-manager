from CredentialsList import CredentialsList
from UI.ListUI import ListUI

class ListController:
    def __init__(self, state):
        self.state = state
        self.credentialsList = CredentialsList()
        self.items = self.credentialsList.getPage(self.state.listPage)
        self.action = None
    
    def mount(self, userInput, ui):
        userInput.setCallback(self.onAction)
        
        self.render(ui)
    
    def onAction(self, action):
        self.action = action
    
    def tick(self, ui):
        if self.action == "keyUp":
            if self.state.listIndex == 0:
                self.state.listIndex = -1
                
                if self.state.listPage == 0:
                    self.state.listPage = self.credentialsList.pages - 1
                else:
                    self.state.listPage -= 1
            else:
                self.state.listIndex -= 1
            
            self.items = self.credentialsList.getPage(self.state.listPage)
            
            if self.state.listIndex == -1:
                self.state.listIndex = self.credentialsList.perPage - 1
        elif self.action == "keyDown":
            if self.state.listIndex == self.credentialsList.perPage - 1:
                self.state.listIndex = 0
                
                if self.state.listPage == self.credentialsList.pages - 1:
                    self.state.listPage = 0
                else:
                    self.state.listPage += 1
            else:
                self.state.listIndex += 1
            
            self.items = self.credentialsList.getPage(self.state.listPage)
        elif self.action == "keyA":
            return "details"
        else:
            return None
        
        self.render(ui)
        
        self.action = None
        
        return None
    
    def render(self, ui):
        ui.render(ListUI(self.items, self.state.listIndex))
