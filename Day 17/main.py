class User:
    id: str
    username: str
    age: int
    
    def __init__(self, id: str = "", username: str = "", age: int = 0):
        self.id = id
        self.username = username
        self.age = age

    def birthday(self):
        self.age += 1
        
    def print_info(self):
        print(f"ID: {self.id}, Username: {self.username}, Age: {self.age}")
        
    
    
    
    
user_1 = User("001", "Pato")

user_1.print_info()

for i in range(10):
    user_1.birthday()
    
user_1.print_info()