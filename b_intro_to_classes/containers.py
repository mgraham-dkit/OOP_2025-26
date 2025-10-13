class Container:
    def __init__(self, name, port, env, username, password):
        self.name = name
        self.port = port
        self.env = env
        self._username = username
        self.__password = password

    def change_password(self, user, old_pass, new_pass):
        # LOGIC!!
        if old_pass == self.__password and user == self._username:
            self.__password = new_pass
            return True
        else:
            return False

    def display(self):
        print(f"Container[name={self.name}, port={self.port}")