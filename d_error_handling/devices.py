from __future__ import annotations

class Device:
    '''
    name
    interface type
    components (list to start, dict later)
    '''
    def __init__(self, name: str, interface: str):
        if name:
            self._name = name

        if interface:
            self._interface = interface

        self.__components = []


    def add_component(self, component: Component) -> None:
        if component.get_interface() != self._interface:
            raise ValueError(f"Component {component.get_name()} employs incorrect interface")

        self.__components.append(component)

    def get_components(self) -> list[Component]:
        return list(self.__components)


class Component:
    '''
    name
    type
    interface type
    job
    '''
    def __init__(self, name: str, type: str, interface: str, job: str):
        if name:
            self._name = name

        if type:
            self._type = type

        if interface:
            self._interface = interface

        if job:
            self._job = job

    def get_interface(self) -> str:
        return str(self._interface)

    def get_name(self) -> str:
        return str(self._name)