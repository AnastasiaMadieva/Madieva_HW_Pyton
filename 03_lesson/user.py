class User:
    def __init__ (self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def getFirstName (self):
        return self.first_name
    
    def getLastName (self):
        return self.last_name
    
    def getName (self):
        return f"Имя: {self.first_name}, Фамилия: {self.last_name}"