from containers import Container

def create_container():
    print("Now creating a container!")
    name = input("Container name: ")
    port = int(input("Operating port: "))
    env = input("Environment details: ")
    username = input("Username: ")
    password = input("Password: ")

    container = Container(name, port, env, username, password)

    return container


containers = []
for i in range(1):
    c = create_container()
    containers.append(c)

for c in containers:
    print(c.__password)
    c.display()

