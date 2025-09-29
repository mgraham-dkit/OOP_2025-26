class Container:
    def __init__(self, name, port, env, username, password):
        self.name = name
        self.port = port
        self.env = env
        self.username = username
        self.password = password

    def change_password(self, user, old_pass, new_pass):
        # LOGIC!!
        if old_pass == self.password and user == self.username:
            self.password = new_pass
            return True
        else:
            return False

    def display(self):
        print(f"Container[name={self.name}, port={self.port}")