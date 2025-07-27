class User:
    def __init__(self, first_name, last_name, id):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.login_attemts = 0
    
    def describe_user(self):
        print(f"あなたの名前は {self.first_name.title()} {self.last_name.title()} です。")
        print(f"あなたの ID は {self.id} です。")
    
    def greet_user(self):
        print(f"こんにちは {self.first_name.title()} {self.last_name.title()} !")

    def reset_login_attempts(self):
        self.login_attemts = 0
    
    def increment_login_attempts(self):
        self.login_attemts += 1

