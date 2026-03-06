from devices import Device
from devices import Component


def create_component() -> Component:
    name = input("Enter component name: ")
    c_type = input("Enter component type: ")
    interface = input("Enter component interface: ")
    job = input("Enter component job: ")

    component = Component(name, c_type, interface, job)
    return component


if __name__ == "__main__":
    my_machine = Device("My laptop", "USB-C")
    components = []

    for i in range(2):
        component = create_component()
        components.append(component)

    for component in components:
        my_machine.add_component(component)


