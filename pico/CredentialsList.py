from Credentials import Credentials
import math
from phew.server import file_exists

class CredentialsList:
    def __init__(self):
        file = self.file()

        self.length = sum(1 for line in file if line.rstrip())
        
        file.close()
    
    def file(self):
        if not file_exists('passwords.csv'):
            file = open('passwords.csv', 'w')
            file.write('')
            file.close()

        return open('passwords.csv', 'r')

    def getItems(self, state):
        items = []
        startIndex = state.index - state.listIndex
        endIndex = startIndex + 5
        index = 0
        file = self.file()
        
        for line in file:
            if not line.rstrip(): continue

            if index >= startIndex and index < endIndex:
                dataArray = line.rstrip('\n').rstrip('\r').split('\t')
                item = Credentials(dataArray)
                
                items.append(item)
            
            index += 1
        
        file.close()

        return items