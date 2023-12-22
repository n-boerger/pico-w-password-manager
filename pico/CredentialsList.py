from Credentials import Credentials
import math
from phew.server import file_exists

class CredentialsList:
    def __init__(self):
        self.currentPage = 0
        self.maxPerPage = 5
        self.perPage = self.maxPerPage
        
        file = self.file()
        self.pages = math.ceil(sum(1 for line in file if line.rstrip()) / self.maxPerPage)
        
        file.close()
    
    def file(self):
        if not file_exists('passwords.csv'):
            file = open('passwords.csv', 'w')
            file.write('')
            file.close()

        return open('passwords.csv', 'r')
    
    def getPage(self, page):
        if page > self.pages:
            return
        
        self.currentPage = page
        
        items = []
        startIndex = self.currentPage * self.maxPerPage
        endIndex = startIndex + self.maxPerPage
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
        
        self.perPage = len(items)
        
        return items