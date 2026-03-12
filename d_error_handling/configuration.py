import logging

from devices import Device, DeviceInterfaceError
from devices import Component


def create_component() -> Component:
    print("Creating new component: ")
    name = input("Enter component name: ")
    c_type = input("Enter component type: ")
    interface = input("Enter component interface: ")
    job = input("Enter component job: ")
    print()

    component = Component(name, c_type, interface, job)
    return component


if __name__ == "__main__":
    logger = logging.getLogger(__name__)

    my_machine = Device("My laptop", "USB-C")
    components = []

    for i in range(2):
        component = create_component()
        components.append(component)

    for component in components:
        try:
            my_machine.add_component(component)
        except DeviceInterfaceError as e:
            logger.error(f"Incompatible interfaces. Component {component.get_name()} not added.")
            #print()
        except ValueError as e:
            print(f"ValueError occurred : {e.args[0]}")
            print(f"Failed to add {component.get_name()}")


