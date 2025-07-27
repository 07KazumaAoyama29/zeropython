from user import User

class Privilages:
    def __init__(self, *previlages):
        self.privilages = previlages
    

class Admin(User):
    def __init__(self, first_name, last_name, id, *privileges):
        super().__init__(first_name, last_name, id)
        self.privileges = Privilages(privileges)
    
    def show_previleges(self):
        print(f"{self.first_name} の権限は以下の通りです。")
        for previlage in self.privileges.privilages:
            print(f"- {previlage}")